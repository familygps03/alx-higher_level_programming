#!/usr/bin/python3
"""Defines a function is_kind_of_class()"""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Args:
        obj: Object to check.
        a_class: Class or a class derived from it.

    Returns:
        bool: True if the object is an instance of the specified class or its
        subclasses, False otherwise.
    """
    return isinstance(obj, a_class)
