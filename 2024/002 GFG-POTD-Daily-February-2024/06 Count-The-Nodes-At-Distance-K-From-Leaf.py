# User function Template for python3

"""
@input - 
node - root node of given tree
k = distance of nodes required 

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

class Solution:
    # Function to return count of nodes at a given distance from leaf nodes.
    def dfs(self, root, stack, k, visiting_node):
        if root:
            stack.append(root)
            if not root.left and not root.right:
                n = len(stack)
                if n > k and (stack[- k - 1] not in visiting_node):
                    visiting_node.add(stack[- k - 1])
            self.dfs(root.left, stack, k, visiting_node)
            self.dfs(root.right, stack, k, visiting_node)
            stack.pop()

    def printKDistantfromLeaf(self, root, k):
        # Code here
        visiting_node = set()
        self.dfs(root, [], k, visiting_node)
        return len(visiting_node)
