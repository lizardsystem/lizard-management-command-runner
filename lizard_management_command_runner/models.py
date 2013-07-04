# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import datetime

from StringIO import StringIO

from django.core import management
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .log_capturer import LogCapturer


class ManagementCommand(models.Model):
    """A management command. Management commands can only run once
    simultaneously."""

    description = models.CharField(
        max_length=100, verbose_name=_("Description"))

    command = models.CharField(
        max_length=30, verbose_name=_("Command"), unique=True)

    max_minutes_to_run = models.IntegerField(
        verbose_name=_("Maximum minutes to run"),
        null=True, blank=True,
        help_text=_(
            "After this length of time, if we still haven't recorded that "
            "the command has finished, we assume something has gone wrong "
            "and it can be restarted again. Always make sure that the "
            "command can't take this long in normal use!"))

    currently_running = models.BooleanField(
        verbose_name=_("Currently running"),
        default=False)

    last_start = models.DateTimeField(
        verbose_name=_("Time of last start"),
        null=True, blank=True)

    class Meta:
        permissions = (
            ("execute_managementcommand",
             _("Can execute management commands")),
            )

    def __unicode__(self):
        return self.command

    def run(self, user):
        """Run this management command (as this user)."""
        # Check that user has access
        if not self.has_access(user):
            return

        # Check that command is ready to run
        if not self.ready_to_run:
            return

        # Mark that command is running
        self.currently_running = True
        self.last_start = datetime.datetime.now()
        self.save()

        # Create a CommandRun object
        command_run = CommandRun.create(self, user)

        log = StringIO()

        # Catch all errors
        try:
            with LogCapturer(buffer=log):
                management.call_command(
                    self.command.encode('utf8'), stdout=log, stderr=log)

            # Finish
            self.finish(command_run, log, success=True)

        except Exception as e:
            # Log exception
            log.write("Caught exception: {exception}\n".format(exception=e))
            self.finish(command_run, log, success=False)

    def finish(self, command_run, log, success):
        command_run.captured_output = log.getvalue()

        command_run.finished = True
        command_run.success = success
        command_run.save()

        self.currently_running = False
        self.save()

    def has_access(self, user):
        return user.has_perm(
            'lizard_management_command_runner.execute_managementcommand')

    @property
    def ready_to_run(self):
        """Command is ready to run if it's not running, or the last run is too
        long ago."""
        if not self.currently_running:
            return True

        if self.max_minutes_to_run is None:
            # Don't use the 'assume it's stopped' feature
            return False

        probable_end = self.last_start + datetime.timedelta(
            minutes=self.max_minutes_to_run)
        if datetime.datetime.now() >= probable_end:
            # Apparently something went wrong
            return True

        return False

    def latest_runs(self, n=5):
        return CommandRun.objects.filter(
            management_command=self)[:n]


class CommandRun(models.Model):
    management_command = models.ForeignKey(ManagementCommand, null=False)

    start_time = models.DateTimeField(auto_now_add=True)

    started_by = models.CharField(max_length=40)  # Name of user

    finished = models.BooleanField(default=False)
    success = models.NullBooleanField(default=None)

    captured_output = models.TextField()

    class Meta:
        ordering = ('-start_time',)

    def __unicode__(self):
        return "Run of '{command}' at {time}".format(
            command=self.management_command,
            time=self.start_time)

    @classmethod
    def create(cls, management_command, user):
        return cls.objects.create(
            management_command=management_command,
            started_by=user.get_full_name())
