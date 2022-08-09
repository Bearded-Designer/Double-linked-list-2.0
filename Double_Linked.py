# the second version of the doubly linked list program that I wrote before
from unittest.mock import NonCallableMagicMock


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Double_Linked:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_before(self, new_data):
        """adds data to the front of the list"""
        new_node = Node(new_data)
        if self.head is None:
            new_node = Node(new_data)
            self.head = new_node
            print(f"list started")
            return
        else:
            print(f"The list is not empty")
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

        self.tail = self.head
        while self.tail.next is not None:
            self.tail = self.tail.next
        self.tail.next = new_node

    def insert_after(self, prev_node, new_data):
        """adds data in the middle of the list"""
        try:

            new_node = Node(new_data)
            prev_node = new_node
            new_node.next = prev_node.next
            new_node.prev = prev_node

        except Exception as e:
            print(e)

    def insert_at_end(self, data):

        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        end = self.head

    def traverse_list(self):

        n = self.head
        while n is not None:
            print(n.data, " ")
            n = n.next

    def del_start(self):
        if self.head is None:
            print(f"no element to delete")
        if self.head.prev is None:
            self.head = None
            return
        self.head = self.head.next
        self.prev = None

    """methods that I need to add in"""
    # def Delete_curr(self, data):

    # def Delete_last(self, data):
    # def Mod_node(self, data):
