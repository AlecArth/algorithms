"""
BinaryTree implementation in Python.
"""

class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def find(self, key):
        if self.root is None:
            return False
        else:
            return self._find(self.root, key)
    
    def _find(self, node, key):
        if node.key == key:
            return True
        if key < node.key:
            if node.left is None:
                return False
            else:
                return self._find(node.left, key)
        elif key > node.key:
            if node.right is None:
                return False
            else:
                return self._find(node.right, key)

    def remove(self, key):
        if self.root is None:
            print("No values in binary tree to delete.")
        else:
            self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if node is None:
            return None
        
        elif node.key == key:
            # Remove leaf node
            if node.left == None and node.right == None:
                return None
            # Remove a node with one child.
            elif node.left == None and node.right != None:
                return node.right
            elif node.right == None and node.left != None:
                return node.left
            # Remove a node with two children.
            else:
                node.key = self._get_smallest_value(node.right)
                node.right = self._remove(node.right, node.key)
                return node
            
        elif node.left != None and key < node.key:
            node.left = self._remove(node.left, key)
            return node
        
        elif node.right != None and key > node.key:
            node.right = self._remove(node.right, key)
            return node

    def _get_smallest_value(self, node):
        if node.left is None:
            return node.key
        return self._get_smallest_value(node.left)

    def print_keys(self):
        keys = []
        self._print_keys(self.root, keys)
        print(f"Keys: {keys}")

    def _print_keys(self, node, keys):
        if node is not None:
            keys.append(node.key)
            if node.left is not None:
                self._print_keys(node.left, keys)
            if node.right is not None:
                self._print_keys(node.right, keys)

    # DFS using recursion.
    def print_keys_dfs(self):
        keys = []
        self._print_keys(self.root, keys)
        print(f"Keys: {keys}")

    def _print_keys_dfs(self, node, keys):
        if node is not None:
            keys.append(node.key)
            if node.left is not None:
                self._print_keys(node.left, keys)
            if node.right is not None:
                self._print_keys(node.right, keys)

    # BFS using a while loop.
    def print_keys_bfs(self):
        keys = []
        queue = []

        queue.append(self.root)
        
        while(len(queue) > 0):
            node = queue.pop(0)
            keys.append(node.key)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        print(f"Keys: {keys}")


if __name__ == '__main__':
    binary_tree = BinaryTree()
    binary_tree.print_keys()
    print(f"\nRemove {20} from binary tree")
    binary_tree.remove(20)

    nums = [20, 15, 18, 10, 25, 24, 27, 19, 17, 28]
    print(f"\nInsert {nums} into binary tree.")
    for num in nums:
        binary_tree.insert(num)
    binary_tree.print_keys()

    print("\nPrint keys using DFS")
    binary_tree.print_keys_dfs()

    print("\nPrint keys using BFS")
    binary_tree.print_keys_bfs()

    nums = [20, 18, 19, 25, 10, 28, 45, 24]
    print(f"\nFind {nums} in binary tree")
    for num in nums:
        print(f"{num}: {binary_tree.find(num)}")

    nums = [20, 18, 19, 25, 10, 28]
    print(f"\nRemove {nums} from binary tree")
    binary_tree.print_keys()
    for num in nums:
        print(f"remove {num}")
        binary_tree.remove(num)
        binary_tree.print_keys()

    nums = [20, 18, 19, 25, 10, 28, 45, 24]
    print(f"\nFind {nums} in binary tree")
    for num in nums:
        print(f"{num}: {binary_tree.find(num)}")

    nums = [45]
    print(f"\nInsert {nums} into binary tree.")
    for num in nums:
        binary_tree.insert(num)
    binary_tree.print_keys()

    nums = [45]
    print(f"\nFind {nums} in binary tree")
    for num in nums:
        print(f"{num}: {binary_tree.find(num)}")
