#!/usr/bin/python3
"""Defines the classes Node and SinglyLinkedList"""

class Node:
    """
    A class that defines properties of a Node.

    Attributes:
        data: Data field of the node.
    """
    def __init__(self, data, next_node=None):
        """
        Creates new instances of a node.

        Args:
            data (int): Data field of the node.
            next_node (Node): Reference to the next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data field of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Property setter for data.

        Args:
            value (int): Data field of the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node instance."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Property setter for next_node.

        Args:
            value (Node): Reference to the next node in the linked list.

        Raises:
            TypeError: If next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """
    A class that defines properties of a Singly Linked List.

    Attributes:
        head: Head of the Singly Linked List.
    """
    def __init__(self):
        """Creates new instances of a Singly Linked List."""
        self.__head = None

    def __str__(self):
        """Represents the class objects as a string.

        Returns:
            str: The class object represented as a string.
        """
        temp_var = self.__head
        print_node = []
        while temp_var:
            print_node.append(str(temp_var.data))
            temp_var = temp_var.next_node

        print_node.sort(key=int)
        return "\n".join(print_node)

    def sorted_insert(self, value):
        """Inserts a new node in sorted order.

        Args:
            value: Value to be inserted.
        """
        if self.__head is None:
            new_node = Node(value)
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            new_node = Node(value)
            new_node.data = value
            new_node.next_node = self.__head
            self.__head = new_node
