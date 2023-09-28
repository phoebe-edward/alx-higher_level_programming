#!/usr/bin/python3
"""Defining class Node"""


class Node:
    """class Node"""
    def __init__(self, data, next_node=None):
        """initializing Node
        Args:
        data: data int
        next_node: next node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if ((value is not None) and (not isinstance(value, Node))):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Defining class SinglyLinkedList"""


class SinglyLinkedList:
    """class SinglyLinkedList"""
    def __init__(self):
        """initializing the SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """inserted Noded in the List in ascending order
        Args:
        value: data to be inserted in new node"""
        n = Node(value)
        if self.__head is None:
            n.next_node = None
            self.__head = n
        elif self.__head.data > value:
            n.next_node = self.__head
            self.__head = n
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            n.next_node = tmp.next_node
            tmp.next_node = n

    def __str__(self):
        """print list"""
        tmp = self.__head
        str_out = ""
        while (tmp is not None):
            str_out += str(tmp.data)
            if tmp.next_node is not None:
                str_out += "\n"
            tmp = tmp.next_node
        return str_out
