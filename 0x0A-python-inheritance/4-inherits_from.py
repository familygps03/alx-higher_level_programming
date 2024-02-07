#!/usr/bin/python3
"""Defines a function inherits_from()"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherits
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class or a class derived from it.

    Returns:
        bool: True if the object is an instance of a subclass of the specified
        class, False otherwise.
    """
    return isinstance(obj, type) and issubclass(type(obj), a_class) and type(obj) != a_class
