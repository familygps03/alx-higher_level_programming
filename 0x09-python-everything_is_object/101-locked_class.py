#!/usr/bin/python3
"""Defines a class LockedClass"""


class LockedClass:
    """
    Restricts the user from dynamically creating new instance attributes,
    except if the new instance attribute is named first_name.

    Attributes:
        first_name (str): First name of something.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instances of the LockedClass."""
        self.first_name = "first_name"
