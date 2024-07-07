# User function Template for python3
"""
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

def ancestors(root, target, arr):
    if(root == None):
        return False
    if(root.data == target):
        return True
    leftRoot = ancestors(root.left, target, arr)
    rightRoot = ancestors(root.right, target, arr)
    if(leftRoot or rightRoot):
        arr.append(root.data)
        
    return leftRoot or rightRoot

class Solution:

    def Ancestors(self, root, target):
        """
        :param root: root of the given tree.
        :return: None, print the space separated post ancestors of given target., don't print new line
        """
        # Code here
        arr = []
        ancestors(root, target, arr)
        return arr
