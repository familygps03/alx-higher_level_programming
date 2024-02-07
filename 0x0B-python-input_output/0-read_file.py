#!/usr/bin/python3
"""Module containing the function read_file."""


def read_file(filename=""):
    """Reads the content of a file and prints it to stdout.

    Args:
        filename (str, optional): The name of the file to read. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read()
        print(content, end='')
