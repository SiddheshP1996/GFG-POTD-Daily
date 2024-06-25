# User function Template for python3

"""
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""


class Solution:

    def KDistanceNodes(self, root, target, k):
        # code here
        # return the sorted list all nodes at k distance from target
        parentMap = {}
        targetNode = None

        def dfs(root, p):
            if root is None:
                return None
            if root.data == target:
                nonlocal targetNode
                targetNode = root

            parentMap[root.data] = p
            dfs(root.left, root)
            dfs(root.right, root)

        dfs(root, None)
        resultArray = []

        def get_k(root, visited, dist):
            if root is None:
                return
            if root in visited:
                return
            if dist == k:
                resultArray.append(root.data)
                return
            visited.add(root)
            get_k(parentMap[root.data], visited, dist + 1)
            get_k(root.left, visited, dist + 1)
            get_k(root.right, visited, dist + 1)
            visited.discard(root)

        get_k(targetNode, set(), 0)
        resultArray.sort()
        return resultArray
