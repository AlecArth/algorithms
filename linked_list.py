"""
A Linked List.
"""

class Node():
    def __init__(self, value = None):
        self.value = value
        self.next_node = None


class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def find(self, value):
        current_node = self.head
        if current_node == None:
                return None
        if current_node.value == value:
            return current_node

        while current_node.next_node != value:
            current_node = current_node.next_node
            if current_node == None:
                return None
            if current_node.value == value:
                return current_node

    def print_nodes(self):
        if self.head == None:
           print("List is empty")

        current_node = self.head
        while current_node is not None:
            if current_node.next_node != None:
                print(f"{current_node.value}, ", end="")
            else:
                print(f"{current_node.value}")
            current_node = current_node.next_node

    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next_node is None and self.head.value == value:
            self.head.value = None
            print("Head was the only node, node has been deleted")
            return
        if self.head.value == value:
            self.head = self.head.next_node
            print(f"{value} found and deleted. New head is {self.head.value}")
            return
        
        current_node = self.head
        previous_node = None

        # Find the node to delete.
        while current_node != value:
            previous_node = current_node
            current_node = current_node.next_node
            if current_node is None:
                print("Node is None")
                return
            if current_node.value == value:
                break

        # Delete the node.
        previous_node.next_node = current_node.next_node
        print(f"{value} found and deleted.")
        return

if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.print_nodes()

    print("\nInsert numbers into linked list.")
    nums = [3,5,6,2,4]
    for num in nums:
        linkedlist.insert(num)
    linkedlist.print_nodes()

    nums2 = [3, 19, 5, 4, 6]
    print(f"\nFind numbers in the linked list: {nums2}")
    for num2 in nums2:
        node = linkedlist.find(num2)
        if node is not None:
            print(f"Found '{node.value}' in list")
        else:
            print(f"'{num2}' not in list")

    print("\nDelete a number from the linked list.")
    linkedlist.delete(6)
    linkedlist.print_nodes()

    print("\nDelete head node number from the linked list.")
    linkedlist.delete(3)
    linkedlist.print_nodes()

    print("\nDelete tail node number from the linked list.")
    linkedlist.delete(4)
    linkedlist.print_nodes()
