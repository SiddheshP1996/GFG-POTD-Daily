# User function Template for python3

"""
class Node:
    ''' Class Node '''
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""

# Function to convert a binary tree to doubly linked list.
class Solution:
    def bToDLL(self, root):
        # Do Code here
        def dfs(rootNode):
            firstNode = lastNode = rootNode
            
            if rootNode.left:
                firstNode, rootNode.left = dfs(rootNode.left)
                rootNode.left.right = rootNode
            
            if rootNode.right:
                rootNode.right, lastNode = dfs(rootNode.right)
                rootNode.right.left = rootNode
                
            return firstNode, lastNode
            
        return dfs(root)[0]
