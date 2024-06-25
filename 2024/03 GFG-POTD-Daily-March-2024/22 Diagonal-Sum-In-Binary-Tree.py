# User function Template for python3

"""
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    # Complete the function below
    def executeSum(self, root, diagonal, rootMap):
        if not root:
            return
        rootMap[diagonal] = rootMap.get(diagonal, 0) + root.data
        self.executeSum(root.left, diagonal + 1, rootMap)
        self.executeSum(root.right, diagonal, rootMap)

    def diagonalSum(self, root):
        # :param root: root of the given tree.
        # code here
        rootMap = {}
        self.executeSum(root, 0, rootMap)
        result = []
        for key, value in rootMap.items():
            result.append(value)
        return result
