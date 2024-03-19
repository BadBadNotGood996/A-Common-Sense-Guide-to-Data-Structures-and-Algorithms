"""
Linked List Implementation
src: A Common Sense Guide to Data Structures and Algorithms
"""


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:

    def __init__(self, first_node):
        self.first_node = first_node

    def read(self, index):
        # Begin at the first node of the list
        current_node = self.first_node
        current_index = 0

        while current_index < index:
            # Keep following the links of each node until we get to the index
            current_node = current_node.next_node
            current_index += 1

            # If we're past the end of the list return None
            if current_node is None:
                return None

        return current_node.data

    def index_of(self, value):
        # Begin at the first node of the list
        current_node = self.first_node
        current_index = 0

        while current_node is not None:
            # If the data in node is equal to value, return it's index
            if current_node.data == value:
                return current_index

            # Move to the next node
            current_node = current_node.next_node
            current_index += 1

        # If we get through the entire list, return None
        return None

    def insert_at_index(self, index, value):
        # Create the new node with the provided value
        new_node = Node(value)

        # If inserting at the beginning
        if index == 0:
            # New node links to what was the first node
            new_node.next_node = self.first_node
            self.first_node = new_node
            return

        # If we are inserting anywhere than the beginning
        current_node = self.first_node
        current_index = 0

        # Access the node immediately before where the node will go
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1

        # New node links to the next node
        new_node.next_node = current_node.next_node

        # Modify the link of the previous node to point to our new node
        current_node.next_node = new_node

    def delete_at_index(self, index):
        # If deleting the first node
        if index == 0:
            # Set the first node to be what is currently the second node
            self.first_node = self.first_node.next_node
            return

        current_node = self.first_node
        current_index = 0

        # Find the node immediately before the one we want to delete
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1

        # Find the node that comes after the one we're deleting
        node_after_deleted_node = current_node.next_node.next_node

        # Change the link of the current_node to point to the
        # node_after_deleted_node, leaving the node we want to delete out of
        # the list
        current_node.next_node = node_after_deleted_node


node_1 = Node('once')
node_2 = Node('upon')
node_3 = Node('a')
node_4 = Node('time')

node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

list = LinkedList(node_1)

print(list.read(2))
print(list.index_of("time"))

list.insert_at_index(3, "purple")

print(list.read(0))
print(list.read(1))
print(list.read(2))
print(list.read(3))
print(list.read(4))
print(list.read(5))

list.delete_at_index(3)

print(list.read(0))
print(list.read(1))
print(list.read(2))
print(list.read(3))
print(list.read(4))
print(list.read(5))
