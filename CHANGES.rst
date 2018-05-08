Changelog of lizard-management-command-runner
===================================================


0.3 (unreleased)
----------------

- Nothing changed yet.


0.2 (2018-05-08)
----------------

- Update to Django 1.11, Celery 4

- Regenerate migrations

- Fix the live log capturer


0.1 (2013-07-07)
----------------

- Initial project structure created with nensskel 1.34.dev0.

- Add models for ManagementCommands and CommandRuns.

- We can now define commands, run them with Celery, and capture all
  output (from stdout, stderr and logging). Success and captured
  output are saved in the CommandRun objects.

- There is a page where commands can be started and logs can be shown.
