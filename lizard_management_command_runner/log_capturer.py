# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-

""" """

# Python 3 is coming
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

"""Context manager that helps capturing logging."""


import logging
from StringIO import StringIO


class LogCapturer(object):
    def __init__(self, buffer=None, format="%(levelname)s: %(message)s"):
        """It is possible to give an optional buffer, otherwise a fresh one
        is used. The buffer's contents are accessible afterwards with
        logcapturer.buffer.getvalue()."""
        if buffer is None:
            self.buffer = StringIO()
        else:
            self.buffer = buffer

        self.format = format

    def __enter__(self, buffer=None):
        """Add the new handler."""

        # Create new handler, set its formatter
        self.logHandler = logging.StreamHandler(self.buffer)
        formatter = logging.Formatter(self.format)
        self.logHandler.setFormatter(formatter)

        # Add it
        rootLogger = logging.getLogger()
        rootLogger.addHandler(self.logHandler)

        # Returning self makes 'with LogCapturer() as ...' possible.
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Remove the handler.
        rootLogger = logging.getLogger()
        rootLogger.removeHandler(self.logHandler)

        self.logHandler.flush()
        self.buffer.flush()  # In case it's something flushable
