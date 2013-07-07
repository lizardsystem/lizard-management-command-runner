# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin
from lizard_ui.urls import debugmode_urlpatterns

from lizard_management_command_runner import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.CommandPageView.as_view(), name='command_page_view'),
    url(r'^command/(?P<command_id>\d+)/$',
        views.run_command, name="command_run_view"),
    url(r'^runs/$',
        views.last_run_of_all_commands, name="latest_runs_view"),
    )
urlpatterns += debugmode_urlpatterns()
