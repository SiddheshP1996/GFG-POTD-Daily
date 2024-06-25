# User function Template for python3

"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

class Solution:
    # Function to find the minimum element in the given BST.
    def minValue(self, root):
        # Your code here
        if root is None:
            return -1
            
        currentNode = root
        while currentNode.left is not None:
            currentNode = currentNode.left
        
        return currentNode.data
