# User function Template for python3

"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    # Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        # Code here
        def inorder(root, result):
            if root:
                inorder(root.left, result)
                result.append(root.data)
                inorder(root.right, result)
        result = []
        inorder(root, result)
        
        return result
    
    # Function to deserialize a list and construct the tree.   
    def deSerialize(self, a):
        # Code here
        def helper(a, leftNode, rightNode):
            if leftNode > rightNode:
                return
            
            index = (leftNode + rightNode) // 2
            
            root = Node(a[index])
            
            root.left = helper(a, leftNode, index - 1)
            root.right = helper(a, index + 1, rightNode)
            return root
        return helper(a, 0, len(a) - 1)
