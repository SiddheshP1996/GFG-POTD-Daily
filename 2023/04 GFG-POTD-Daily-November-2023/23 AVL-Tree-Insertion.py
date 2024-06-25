# User function Template for python3

"""
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        self.height = 1
"""


class Solution:
    def getTreeHeight(self, node):
        return 0 if not node else node.height

    def updateTreeHeight(self, node):
        if not node:
            return 0
        node.height = 1 + max(self.getTreeHeight(node.left), self.getTreeHeight(node.right))
        return node.height

    def getTreeBalance(self, root):
        return 0 if not root else (self.getTreeHeight(root.left) - self.getTreeHeight(root.right))

    def rotateToTheLeft(self, root):
        y = root.right
        root.right = y.left
        y.left = root
        self.updateTreeHeight(root)
        self.updateTreeHeight(y)
        return y

    def rotateToTheRight(self, root):
        y = root.left
        root.left = y.right
        y.right = root
        self.updateTreeHeight(root)
        self.updateTreeHeight(y)
        return y

    def insertToAVL(self, root, key):
        if not root:
            return Node(key)

        if key < root.data:
            root.left = self.insertToAVL(root.left, key)
        else:
            root.right = self.insertToAVL(root.right, key)

        self.updateTreeHeight(root)
        balance = self.getTreeBalance(root)

        # Left Heavy
        if balance > 1:
            # Left-Left case
            if key < root.left.data:
                return self.rotateToTheRight(root)
            # Left-Right case
            if key > root.left.data:
                root.left = self.rotateToTheLeft(root.left)
                return self.rotateToTheRight(root)

        # Right Heavy
        if balance < -1:
            # Right-Right case
            if key > root.right.data:
                return self.rotateToTheLeft(root)
            # Right-Left case
            if key < root.right.data:
                root.right = self.rotateToTheRight(root.right)
                return self.rotateToTheLeft(root)

        return root
