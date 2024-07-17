# User function Template for python3

"""
# A node structure
class Node:
    A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
"""

class Solution:
    # Function to construct binary tree from parent array.
    def createTree(self, parent):
        # Your code here
        numberOfParent = len(parent)
        nodes = [Node(i) for i in range(numberOfParent)]
        root = None
        
        for i in range(numberOfParent):
            if parent[i] == -1:
                root = nodes[i]
            else:
                if nodes[parent[i]].left is None:
                    nodes[parent[i]].left = nodes[i]
                else:
                    nodes[parent[i]].right = nodes[i]
        
        return root
