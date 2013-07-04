# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.http import HttpResponse
from django.utils.translation import ugettext as _

from lizard_ui.views import UiView

from lizard_management_command_runner import models
from lizard_management_command_runner import tasks


class CommandPageView(UiView):
    template_name = "lizard_management_command_runner/command_page.html"

    def commands(self):
        return [
            command for command in models.ManagementCommand.objects.all()
            if command.has_access(self.request.user)
            ]


def run_command(request, command_id):
    if request.method != "POST":
        return

    try:
        command = models.ManagementCommand.objects.get(pk=command_id)
    except models.ManagementCommand.DoesNotExist:
        return

    tasks.run_management_command.delay(request.user, command)
    return HttpResponse()
