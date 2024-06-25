# User function Template for python3


"""
class Node:
# Constructor to create a new Node
def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
"""


# Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self, root):

        # add code here
        if root is None:
            return True
        cacheData = {}

        def getHeight(root):
            if root is None:
                return 0
            if root in cacheData:
                return cacheData[root]
            ans = 1 + max(getHeight(root.left), getHeight(root.right))
            cacheData[root] = ans
            return ans

        return abs(getHeight(root.left) - getHeight(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)
