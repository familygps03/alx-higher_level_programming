#!/usr/bin/python3
"""Defines a class MyInt that inherits from int.
MyInt is a rebel. MyInt has == and != operators inverted
"""


class MyInt(int):
    """Defines a class MyInt, with inverted equality operators.

    Args:
        int (int): Value.
    """
    def __init__(self, value):
        """Creates a new instance of class MyInt.

        Args:
            value (int): Integer value.
        """
        super().__init__(value)

    def __eq__(self, other):
        """Override the equality operator.

        Args:
            other (int): Another integer.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator.

        Args:
            other (int): Another integer.

        Returns:
            bool: True if equal, False otherwise.
        """
        return super().__eq__(other)
