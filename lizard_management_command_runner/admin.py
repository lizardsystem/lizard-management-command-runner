# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.contrib import admin

from lizard_management_command_runner import models


admin.site.register(models.ManagementCommand)
admin.site.register(models.CommandRun)
