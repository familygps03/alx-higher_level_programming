#!/usr/bin/python3
"""Module defining the class Student based on 10-student.py"""


class Student:
    """
    Class that defines properties of a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """Creates a new instance of Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes whose names are
        contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.

        Args:
            attrs (list, optional): A list of strings representing attribute
            names to retrieve. Defaults to None.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__

        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary containing attribute-value pairs.
        """
        self.__dict__.update(json)
