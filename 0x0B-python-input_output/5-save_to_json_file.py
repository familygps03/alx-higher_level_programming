#!/usr/bin/python3
"""Module containing the function save_to_json_file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a JSON file.

    Args:
        my_obj (any): The object to write to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
