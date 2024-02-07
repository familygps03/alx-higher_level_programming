#!/usr/bin/python3
"""Function add_attribute"""


def add_attribute(obj, attr_name, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (object): The object to which the attribute will be added.
        attr_name (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Cannot add a new attribute")
    setattr(obj, attr_name, value)
