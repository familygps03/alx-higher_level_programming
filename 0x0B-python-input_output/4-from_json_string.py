#!/usr/bin/python3
"""Module containing the function from_json_string."""
import json


def from_json_string(my_str):
    """Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        any: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
