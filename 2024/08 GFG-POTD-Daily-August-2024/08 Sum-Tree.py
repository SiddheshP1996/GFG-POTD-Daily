# User function Template for python3

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

class Solution:
    def execute(self, root):
        if not root: return [True, 0]
        
        if not root.left and not root.right: return [True, root.data]
        
        leftTree = self.execute(root.left)
        
        rightTree = self.execute(root.right)
        
        treeSum = leftTree[1] + rightTree[1]
        
        if leftTree[0] and rightTree[0] and root.data == treeSum:
            return [True, root.data * 2]
        
        return [False, leftTree[1] + rightTree[1]]
        
    def is_sum_tree(self, node):
        # Code here
        return self.execute(node)[0]
