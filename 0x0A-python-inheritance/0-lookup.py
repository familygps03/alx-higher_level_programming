#!/usr/bin/python3
"""Module containing the function lookup"""


def lookup(obj):
    """Returns the list of attributes and methods of an object.

    Args:
        obj (object): Object to inspect.

    Returns:
        list: List of available attributes and methods.
    """
    return dir(obj)
