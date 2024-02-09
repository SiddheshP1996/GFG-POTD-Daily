# User function Template for python3

"""
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    # Function to check whether all nodes of a tree have the value 
    # Equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # Code here
        if not root or (not root.left and not root.right):
            return 1
       
        left_node, right_node, summ = 1, 1, 0
       
        if root.left:
            left_node = self.isSumProperty(root.left)
            summ += root.left.data
        if root.right:
            right_node = self.isSumProperty(root.right)
            summ += root.right.data
       
        return int(root.data == summ) and left_node and right_node
