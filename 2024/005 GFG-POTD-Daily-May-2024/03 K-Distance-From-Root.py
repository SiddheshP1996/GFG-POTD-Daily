# User function Template for python3

"""
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def KDistance(self, root, k):
        """
        :param root: root of given tree.
        :param k: distance k from root
        :return: list of all nodes that are at distance k from root.
        """
        # Code here
        result = []
        
        def execute(root, distance):
            if not root:
                return 
            
            if distance == k:
                result.append(root.data)
                return 
            
            execute(root.left,  distance + 1)
            execute(root.right, distance + 1)
            
        execute(root, 0)
        
        return result
