from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.contrib.auth.models import User
from .models import ManagementCommand


@shared_task
def add(x, y):
    """Add two numbers, useful in testing."""
    return x + y


@shared_task
def run_management_command(user_id, management_command_id):
    user = User.objects.get(pk=user_id)
    command = ManagementCommand.objects.get(pk=management_command_id)
    command.run(user)
