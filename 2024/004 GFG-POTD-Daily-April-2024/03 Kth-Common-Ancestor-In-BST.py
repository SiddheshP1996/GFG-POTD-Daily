# User function Template for python3

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

class Solution:
    def kthCommonAncestor(self, root, k, x, y):
        # Code here
        l = []
        while True:
            l.append(root.data)
            if root.data < x and root.data < y:
                root = root.right
            elif root.data > x and root.data > y:
                root = root.left
            else:
                break
        return -1 if len(l) < k else l[-k]
