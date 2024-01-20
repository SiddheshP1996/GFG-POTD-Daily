# User function Template for python3

"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

class Solution:
    def distributeCandy(self, root):
        # Code here
        self.moves = 0
        def deep_search(root):
            if not root:
                return 0
                
            left_child_candy = deep_search(root.left)
            right_child_candy = deep_search(root.right)
            
            self.moves += abs(left_child_candy) + abs(right_child_candy)
            remaining_candy = left_child_candy + right_child_candy + root.data - 1
            
            return remaining_candy  
        deep_search(root)
        return self.moves
