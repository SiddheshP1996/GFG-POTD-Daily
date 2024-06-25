# User function Template for python3



"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
"""

# Function to return a tree created from postorder and inoreder traversals.
class Solution:
    def buildTree(self, In, post, n):
        # Your code here
        if not In or not post:
            return None
            
        rootValue = post.pop()
        root = Node(rootValue)
        index = In.index(rootValue)
        
        root.right = self.buildTree(In[index + 1:], post, n)
        root.left = self.buildTree(In[:index], post, n)
        
        return root
