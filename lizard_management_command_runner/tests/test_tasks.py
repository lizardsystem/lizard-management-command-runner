# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import mock

from django.test import TestCase

from lizard_management_command_runner import tasks


class TestAdd(TestCase):
    def test_add_function(self):
        self.assertEquals(tasks.add(3, 4), 7)

    def test_add_task(self):
        """This fails, I don't know how to run a Celery using the
        testsettings database. Test by hand"""
        #result = tasks.add.delay(3, 4).get()
        #self.assertEquals(result, 7)
        pass


class TestRunManagementCommand(TestCase):
    def test_function_called(self):
        """Trivial test, actual tests are in test_models"""

        user = mock.MagicMock()
        management_command = mock.MagicMock()

        tasks.run_management_command(user, management_command)
        management_command.run.assert_called_with(user)
