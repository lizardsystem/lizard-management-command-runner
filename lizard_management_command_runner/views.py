# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.utils.translation import ugettext as _

from lizard_ui.views import UiView

from lizard_management_command_runner import models


class CommandPageView(UiView):
    template_name = "lizard_management_command_runner/command_page.html"
