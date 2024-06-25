# User function Temporarylate for python3

from collections import defaultdict

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
    def verticalSum(self, root):
        # :param root: root of the given tree.
        
        # Code here
        temporary = defaultdict(int)
        def execute(root, position):
            if root == None:
                return 
            temporary[position] += root.data
            execute(root.left, position - 1)
            execute(root.right, position + 1)
        
        execute(root, 0)
        extra = sorted(temporary)
        return [temporary[one] for one in extra]
