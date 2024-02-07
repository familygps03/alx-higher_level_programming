#!/usr/bin/python3
"""Module containing the function class_to_json"""


def class_to_json(obj):
    """Returns a dictionary representing the attributes of an object
    suitable for JSON serialization.

    Args:
        obj: An object whose attributes are to be serialized.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    return obj.__dict__
