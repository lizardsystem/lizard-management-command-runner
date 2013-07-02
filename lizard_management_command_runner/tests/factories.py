import factory

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from lizard_management_command_runner import models


class ManagementCommandFactory(factory.Factory):
    FACTORY_FOR = models.ManagementCommand

    description = "A test management command"
    command = "test_management_command"
    max_minutes_to_run = 60
    currently_running = False
    last_start = None


def permission_factory(model, codename):
    ct, created = ContentType.objects.get_or_create(
        app_label='lizard_management_command_runner', model=model)

    p, created = Permission.objects.get_or_create(
        codename=codename, content_type=ct)
    if not created:
        p.name = "Some permission name"
        p.save()

    return p
