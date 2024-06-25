# User function Template for python3

from collections import deque

class Solution:
    # Function to return the level order traversal of a tree.
    def levelOrder(self, root):
        # Code here
        queue = deque([root])
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return result
