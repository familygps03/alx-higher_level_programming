#!/usr/bin/python3
"""Module containing the function write_file."""


def write_file(filename="", text=""):
    """Writes text to a file and returns the number of characters written.

    Args:
        filename (str, optional): The name of the file. Defaults to "".
        text (str, optional): The text to write to the file. Defaults to "".

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        """This method returns the number of characters written to a file."""
        return file.write(text)
