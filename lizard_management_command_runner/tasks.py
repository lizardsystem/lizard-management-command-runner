from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def add(x, y):
    """Add two numbers, useful in testing."""
    return x + y


@shared_task
def run_management_command(user, management_command):
    management_command.run(user)
