# User function Template for python3

"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

"""


class Solution:

    def __init__(self):
        self.head = None
        self.prev = None

    # Function to convert binary tree into circular doubly linked list.
    def bTreeToClist(self, root):
        # Your code here
        if root is None:
            return None

        self.bTreeToClist(root.left)

        if self.prev is None:
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root

        self.prev = root
        self.bTreeToClist(root.right)

        if self.prev.right is None:
            self.head.left = self.prev
            self.prev.right = self.head
        return self.head
