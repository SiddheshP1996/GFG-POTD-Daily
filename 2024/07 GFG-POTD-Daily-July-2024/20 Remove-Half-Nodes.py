# User function Template for python3

class Solution:
    def RemoveHalfNodes(self, node):
        # Code here
        if not node or (not node.left and not node.right):
            return node
        
        node.left = self.RemoveHalfNodes(node.left)
        node.right = self.RemoveHalfNodes(node.right)
        
        if not node.left:  
            return node.right
        
        if not node.right:
            return node.left
        
        return node
