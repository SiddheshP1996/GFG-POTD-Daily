# User function Template for python3

# Structure of node
"""
class Node:
    def __init__(self, data=0):
        self.data=0
        self.left=None
        self.right=None
"""

class Solution:
    def sumOfLeafNodes(self, root):
        # Your code here
        if not root:
            return 0
        
        if not (root.left or root.right):
            return root.data
            
        node1 = self.sumOfLeafNodes(root.left)
        node2 = self.sumOfLeafNodes(root.right)
        return node1 + node2
