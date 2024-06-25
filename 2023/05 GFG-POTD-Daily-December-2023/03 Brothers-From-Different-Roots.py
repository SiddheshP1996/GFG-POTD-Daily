# User function Template for python3

from collections import Counter

"""
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""


class Solution:
    def countPairs(self, root1, root2, x):
        # code here.
        nodeList1 = []
        nodeList2 = []

        def inOrderTraversal(root, listStorageOfNodes):
            if root is None:
                return
            inOrderTraversal(root.left, listStorageOfNodes)
            listStorageOfNodes.append(root.data)
            inOrderTraversal(root.right, listStorageOfNodes)

        inOrderTraversal(root1, nodeList1)
        inOrderTraversal(root2, nodeList2)

        dictionaryOfNodes = Counter(nodeList2)
        counter = 0
        for i in nodeList1:
            currentNode = x - i
            if currentNode in dictionaryOfNodes and dictionaryOfNodes[currentNode] > 0:
                counter += 1
                dictionaryOfNodes[currentNode] -= 1

        return counter
