# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import datetime

from django.test import TestCase
from django.contrib.auth import models as authmodels

from . import factories

from lizard_management_command_runner import models


class TestManagementCommand(TestCase):
    def test_anonymous_user_no_access(self):
        user = authmodels.AnonymousUser()
        managementcommand = factories.ManagementCommandFactory()
        self.assertFalse(managementcommand.has_access(user))

    def test_user_with_permission_can(self):
        group = authmodels.Group.objects.create(name="testusers")
        permission = factories.permission_factory(
            'ManagementCommand', 'execute_managementcommand')
        group.permissions.add(permission)

        user = authmodels.User.objects.create()
        group.user_set.add(user)

        managementcommand = factories.ManagementCommandFactory()
        self.assertTrue(managementcommand.has_access(user))

    def test_command_ready_if_not_running(self):
        managementcommand = factories.ManagementCommandFactory(
            currently_running=False)

        self.assertTrue(managementcommand.ready_to_run)

    def test_command_not_ready_if_running_no_max_time(self):
        managementcommand = factories.ManagementCommandFactory(
            currently_running=True, max_minutes_to_run=None)

        self.assertFalse(managementcommand.ready_to_run)

    def test_command_not_ready_if_recently_running(self):
        managementcommand = factories.ManagementCommandFactory(
            currently_running=True,
            max_minutes_to_run=60,
            last_start=datetime.datetime.now())
        self.assertFalse(managementcommand.ready_to_run)

    def test_command_ready_if_running_too_long_ago(self):
        managementcommand = factories.ManagementCommandFactory(
            currently_running=True,
            max_minutes_to_run=60,
            last_start=(
                datetime.datetime.now() - datetime.timedelta(minutes=120)))
        self.assertTrue(managementcommand.ready_to_run)

    def test_run(self):
        group = authmodels.Group.objects.create(name="testusers")
        permission = factories.permission_factory(
            'ManagementCommand', 'execute_managementcommand')
        group.permissions.add(permission)

        user = authmodels.User.objects.create()
        group.user_set.add(user)

        managementcommand = factories.ManagementCommandFactory(
            command="check_config")

        log = managementcommand.run(user)
        self.assertTrue("INFO: Running checker" in log)


class TestCommandRun(TestCase):
    def test_create_creates_object_in_database(self):
        existing = models.CommandRun.objects.all().count()

        user = authmodels.User(first_name="Test", last_name="User")

        command = factories.ManagementCommandFactory.create()

        models.CommandRun.create(command, user)

        self.assertEquals(
            models.CommandRun.objects.all().count(),
            existing + 1)
