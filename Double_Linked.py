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
        if prev_node is None:
            print(f"This node does not exist")
            return

        new_node = Node(new_data)
        prev_node = new_node
        new_node.next = prev_node.next
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

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

    def del_end(self):
        """if the list has 1 element delete that, otherwise iterate through the list"""
        if self.head.next is None:
            print(f"Nothing in the list")
            return
        if self.head.next is None:
            self.head.next = None
            return

    """methods that I need to add in"""
    # find a node based on the data contained in it
    """search the list and return the position of the variable that was found. for loop and count the numbers until a position is hit and add it to the counter"""

    def find_node(self, value):
        """iterates through the list and finds every position that has that data in it."""
        n = 1
        flag = False

        if self.head == None:
            print(f"list is empty")
            return

        while self.head != None:
            if self.head.data == value:
                flag = True
                break
            self.head = self.head.next
            n = n + 1
        if flag:
            print(f"data is present in the list at position " + str(n))
        else:
            print(f"data is not present in the string")

    def printList(self, node):

        print("\nTraversal in forward direction")
        while node:
            print(" {}".format(node.data))
            last = node
            node = node.next

        print("\nTraversal in reverse direction")
        while last:
            print(" {}".format(last.data))
            last = last.prev


# dlist = Double_Linked()
# dlist.insert_before(10)
# dlist.insert_at_end(8)
# dlist.insert_after(dlist.head.next, 19)
# dlist.insert_at_end(10)

# print(dlist.traverse_list)
# dlist.find_node(10)
# dlist.printList(dlist.head)
