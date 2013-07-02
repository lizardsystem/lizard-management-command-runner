import logging
from StringIO import StringIO

from django.test import TestCase

from lizard_management_command_runner import log_capturer


class TestLogCapturer(TestCase):
    def test_log_something_and_see_if_it_is_returned(self):
        logger = logging.getLogger(__name__)

        with log_capturer.LogCapturer() as capturer:
            logger.debug("Whee!")

        self.assertEquals(
            capturer.buffer.getvalue(),
            "DEBUG: Whee!\n")

    def test_mixing_logs_and_other_buffering(self):
        logger = logging.getLogger(__name__)
        log = StringIO()

        with log_capturer.LogCapturer(buffer=log):
            log.write("ONE\n")
            logger.debug("TWO")
            log.write("THREE")

        result = log.getvalue()

        self.assertTrue(
            result.index("ONE") < result.index("TWO") < result.index("THREE"))
