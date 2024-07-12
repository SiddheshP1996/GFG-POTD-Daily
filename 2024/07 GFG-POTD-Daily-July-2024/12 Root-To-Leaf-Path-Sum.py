# User function Template for python3

"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
"""


class Solution:

    def hasPathSum(self, root, target):
        """
        :param root: root of given tree.
        :param sm: root to leaf sum
        :return: true or false
        """
        # Code here
        if not root:
            return False

        if not root.left and not root.right:
            return target == root.data

        target -= root.data

        return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)
