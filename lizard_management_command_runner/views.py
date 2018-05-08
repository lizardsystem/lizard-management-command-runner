# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import json

from django.http import HttpResponse
from django.utils.translation import ugettext as _

from lizard_ui.views import UiView

from lizard_management_command_runner import models
from lizard_management_command_runner import tasks

from django.contrib.auth.decorators import permission_required


class CommandPageView(UiView):
    template_name = "lizard_management_command_runner/command_page.html"

    def commands(self):
        return [
            command for command in models.ManagementCommand.objects.all()
            if command.has_access(self.request.user)
            ]


@permission_required('lizard_management_command_runner.execute_managementcommand')
def run_command(request, command_id):
    if request.method != "POST":
        return

    tasks.run_management_command.delay(request.user.pk, command_id)
    return HttpResponse()


def last_run_of_all_commands(request):
    return HttpResponse(json.dumps([
            {
                'runid': run.id,
                'command': run.management_command.command,
                'time': (run.start_time.strftime("%d/%m/%y %H:%M")
                         if run.start_time else ""),
                'finished': run.finished,
                'success': run.success,
                'user': run.started_by,
                'output': run.captured_output,
                }
            for run in models.CommandRun.latest_runs(request.user)]))
