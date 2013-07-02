from celery.task import task


@task
def add(x, y):
    """Add two numbers, useful in testing."""
    return x + y


@task
def run_management_command(user, management_command):
    management_command.run(user)
