#!/usr/bin/python3

""" Class definition for linked list"""


class Node:
    """Node for a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): Data part of new Node.
            next_node (Node): Ptr to the next Node.
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """The data property."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """The next_node property."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly-linked list."""

    def __init__(self):
        """Assign head to sll(init)"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted
        position in the list (increasing order).
        Args:
            value (Node): The new Node to insert.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """Print Singly Linked List."""
        values = []
        temp = self.__head

        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
