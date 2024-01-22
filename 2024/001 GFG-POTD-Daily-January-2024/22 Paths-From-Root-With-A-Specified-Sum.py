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
    def help(self, root, sum, list_of_node, result):
        if root:
            sum -= root.data
            list_of_node.append(root.data)
            if sum == 0:
                result.append(list_of_node.copy())
            self.help(root.left, sum, list_of_node, result)
            self.help(root.right, sum, list_of_node, result)
            list_of_node.pop()

    def printPaths(self, root, sum):
        # Code here
        result = []
        list_of_node = []
        self.help(root, sum, list_of_node, result)
        return result
