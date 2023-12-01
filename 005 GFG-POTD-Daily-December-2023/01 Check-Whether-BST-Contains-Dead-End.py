# Solution No 1

# User function Template for python3
# Your task is to complete this function.
# Function should return true/false or 1/0
class Solution:

    def deadEndHelper(self, root, visitedNodes):
        if root is None: return False
        visitedNodes.add(root.data)
        left = self.deadEndHelper(root.left, visitedNodes)
        right = self.deadEndHelper(root.right, visitedNodes)
        if root.left is None and root.right is None:
            if (root.data - 1 <= 0 or root.data - 1 in visitedNodes) and root.data + 1 in visitedNodes:
                return True
        return left or right

    def isDeadEnd(self, root):
        # Code here
        return self.deadEndHelper(root, set())


# Solution No 2

"""
# User function Template for python3
# Your task is to complete this function
# function should return true/false or 1/0
class Solution:

    def deadEndHelper(self, root, visitedNodes):
        if root == None: return False
        visitedNodes.add(root.data)
        left = self.deadEndHelper(root.left, visitedNodes)
        right = self.deadEndHelper(root.right, visitedNodes)
        if root.left == None and root.right == None:
            if (root.data - 1 <= 0 or root.data - 1 in visitedNodes) and root.data + 1 in visitedNodes:
                return True
        return left or right

    def isDeadEnd(self, root):
        # Code here
        return self.deadEndHelper(root, set())
"""
