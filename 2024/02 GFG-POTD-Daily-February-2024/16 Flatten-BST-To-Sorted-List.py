# User function Template for python3
import sys
sys.setrecursionlimit(10 ** 5)

"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""


def inorder(root):
    result = []
    if root.left:
        result += inorder(root.left)
    result.append(root.data)
    
    if root.right:
        result += inorder(root.right)
    return result


class Solution:
    def flattenBST(self, root):
        # Code here
        arrayBST = inorder(root)
        headNode = Node(arrayBST[0])
        iteration = headNode
        for element in range(1, len(arrayBST)):
            temporary = Node(arrayBST[element])
            iteration.right = temporary
            iteration = temporary
        return headNode
