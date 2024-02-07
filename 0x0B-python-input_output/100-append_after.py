#!/usr/bin/python3
"""Module containing the append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text into a file after each line containing a specific string.

    Args:
        filename (str, optional): The name of the file. Defaults to "".
        search_string (str, optional): The string to search for. Defaults to "".
        new_string (str, optional): The string to append. Defaults to "".
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as output_file:
        updated_content = ""
        for line in lines:
            updated_content += line
            if search_string in line:
                updated_content += new_string
        output_file.write(updated_content)
