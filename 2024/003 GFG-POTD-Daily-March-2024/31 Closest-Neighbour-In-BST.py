# User function Template for python3

"""
class Node:
    ''' Class Node '''
    def __init__(self, value):
        self.left = None
        self.key = value
        self.right = None
"""

class Solution:
    def findMaxForN(self, root, n):
        # Print the value of the element if it exists otherwise print -1.
        # Code here
        result = None
        while root:
            if root.key > n:
                root = root.left
            else:
                result = root.key
                root = root.right
        
        return result if result else -1
