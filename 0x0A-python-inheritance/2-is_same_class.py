#!/usr/bin/python3
"""Defines a function is_same_class()"""


def is_same_class(obj, a_class):
    """Check if the object is an instance of the specified class.

    Args:
        obj: Object to check.
        a_class: Class to compare against.

    Returns:
        bool: True if the object is an instance of the class, False otherwise.
    """
    return type(obj) is a_class
