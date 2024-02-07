#!/usr/bin/python3
"""Module containing the function load_from_json_file."""
import json


def load_from_json_file(filename):
    """Loads an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The object loaded from the JSON file.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
