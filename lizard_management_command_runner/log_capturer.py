# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-

""" """

# Python 3 is coming
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

"""Context manager that helps capturing logging."""


from io import BytesIO


class StringIOField(object):
    """
    Write log to a certain field of a Django model instance. Saves the object
    on every call to `write`.
    """
    def __init__(self, obj, field):
        self.stream = BytesIO()
        self.obj = obj
        self.field = field

    def __getattr__(self, item):
        if item != 'stream':
            return getattr(self.stream, item)

    def write(self, *args, **kwargs):
        """
        write(bytes) -> int.  Write bytes to file and save it to the field.

        Return the number of bytes written.
        """
        return_value = self.stream.write(*args, **kwargs)
        setattr(self.obj, self.field, self.stream.getvalue().decode('utf-8'))
        self.obj.save()
        return return_value
