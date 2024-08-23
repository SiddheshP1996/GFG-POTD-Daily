# User function Template for python3

"""
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

# Function to return a list containing elements of left view of the binary tree.
def leftRoot(root, rootLevel, result):
    if not root:
        return
    
    if len(result) == rootLevel:
        result.append(root.data)
        
    leftRoot(root.left, rootLevel + 1, result)
    
    leftRoot(root.right, rootLevel + 1, result)

def LeftView(root):
    # Code here
    result = []
    
    leftRoot(root, 0, result)
    return result
