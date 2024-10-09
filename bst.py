class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, node, key):
        if key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
        else:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.val)
            self._inorder_traversal(node.right, result)
        return result

    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

# Usage example
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(7)
    bst.insert(1)
    bst.insert(5)

    print("Inorder Traversal:", bst.inorder_traversal())  # Output will be the sorted order of the elements
    print("Search for 66:", "Found" if bst.search(66) else "Not Found")
