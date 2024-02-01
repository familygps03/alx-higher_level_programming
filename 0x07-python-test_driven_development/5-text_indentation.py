#!/usr/bin/python3
"""Defines a function that prints a text with 2 new lines after each
of these characters: . ? and :

Attributes:
    print_formatted_text: function that prints a text with specific conditions
"""


def print_formatted_text(text):
    """Prints a text with 2 new lines after .?: characters.

    Args:
        text (str): String to be examined.

    Raises:
        TypeError: If text is not of type str.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
