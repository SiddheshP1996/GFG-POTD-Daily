# User function Template for python3

"""
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
"""

class Solution:
    def sumOfLongRootToLeafPath(self, root):
        # Code here
        def f(root, maxHeight, temporary):
            if root == None:
                return maxHeight, temporary
                
            leftRoot, leftRootSum = f(root.left, maxHeight + 1, temporary + root.data)
            rightRoot, rightRootSum = f(root.right, maxHeight + 1, temporary + root.data)
            
            if leftRoot == rightRoot:
                if leftRootSum > rightRootSum:
                    return leftRoot, leftRootSum
                return rightRoot, rightRootSum
            
            if leftRoot > rightRoot:
                return leftRoot, leftRootSum    
            return rightRoot, rightRootSum
        return f(root, 0, 0)[1]
