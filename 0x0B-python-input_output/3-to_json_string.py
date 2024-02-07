#!/usr/bin/python3
"""Module containing the function to_json_string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object.

    Args:
        my_obj (any): The object to convert to JSON.

    Returns:
        str: The JSON representation of the input object.
    """
    return json.dumps(my_obj)
