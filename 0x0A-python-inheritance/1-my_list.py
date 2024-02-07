#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """Custom list class that inherits from the built-in list class."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
