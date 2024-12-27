"""
This is an implementation of an adjacency list using a dictionary to store linked lists.
"""

from linked_list import LinkedList

class AdjacencyList:
    def __init__(self):
        self.linked_lists = {}

    def insert(self, startKey, endKey=None):
        if startKey not in self.linked_lists or self.linked_lists[startKey] is None:
            self.linked_lists[startKey] = LinkedList()
        if endKey is not None:
            self.linked_lists[startKey].insert(endKey)

    def delete(self, startKey, endKey):
        if startKey in self.linked_lists:
            self.linked_lists[startKey].delete(endKey)
            
            # Remove the reserve connection from the other node.
            if endKey in self.linked_lists:
                self.linked_lists[endKey].delete(startKey)

    def print_lists(self):
        for startKey, linked_list in self.linked_lists.items():
            print(f"Node {startKey}: ", end=" ")
            linked_list.print_nodes()

if __name__ == '__main__':
    adjacency_list = AdjacencyList()
    adjacency_list.print_lists()

    print("\nInsert node connections.")
    adjacency_list.insert(1, 2)
    adjacency_list.insert(1, 5)
    adjacency_list.insert(2, 1)
    adjacency_list.insert(2, 5)
    adjacency_list.insert(2, 3)
    adjacency_list.insert(2, 4)
    adjacency_list.insert(3, 2)
    adjacency_list.insert(3, 4)
    adjacency_list.insert(4, 2)
    adjacency_list.insert(4, 5)
    adjacency_list.insert(4, 3)
    adjacency_list.insert(5, 4)
    adjacency_list.insert(5, 1)
    adjacency_list.insert(5, 2)
    adjacency_list.print_lists()

    print("\nDelete the connection between nodes 2 and 5.")
    adjacency_list.delete(2, 5)
    adjacency_list.print_lists()

    print("\nDelete the connection between nodes 5 and 4.")
    adjacency_list.delete(5, 4)
    adjacency_list.print_lists()

    print("\nDelete the connection between nodes 1 and 5.")
    adjacency_list.delete(1, 5)
    adjacency_list.print_lists()

    print("\nInsert connection between nodes 5 and 4.")
    adjacency_list.insert(5, 4)
    adjacency_list.print_lists()
