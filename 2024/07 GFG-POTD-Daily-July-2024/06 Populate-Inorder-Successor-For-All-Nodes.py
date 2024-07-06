# User function Template for python3

"""
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None
"""

class Solution:

    def populateNext(self, root):
        nodes = []
        def inordertraversal(r, arr):
            if r is None:
                return
            inordertraversal(r.left, arr)
            arr.append(r)
            inordertraversal(r.right, arr)
            return
        inordertraversal(root, nodes)
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]