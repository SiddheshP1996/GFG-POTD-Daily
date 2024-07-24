# User function Template for python3

class Solution:
    
    # Function to check whether a Binary Tree is BST or not.
    def is_BST(self, node, minVal, maxVal):
        if node is None:
            return True
        if not (minVal < node.data < maxVal):
            return False
        return self.is_BST(node.left, minVal, node.data) \
            and self.is_BST(node.right, node.data, maxVal)
    
    def isBST(self, root):
        # Code here
        return self.is_BST(root, float('-inf'), float('inf'))
