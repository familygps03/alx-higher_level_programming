#!/usr/bin/python3
"""Module containing the function append_write."""


def append_write(filename="", text=""):
    """Appends text to a file and returns the number of characters added.

    Args:
        filename (str, optional): The name of the file. Defaults to "".
        text (str, optional): The text to append to the file. Defaults to "".

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        """This method returns the number of characters appended to a file."""
        return file.write(text)
