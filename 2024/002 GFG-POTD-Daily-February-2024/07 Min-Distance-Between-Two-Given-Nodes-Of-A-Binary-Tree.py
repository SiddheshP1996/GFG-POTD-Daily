# User function Template for python3

"""
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def findDist(self, root, a, b):
        # return: minimum distance between a and b in a tree with given root
        # Code here
        def nodeDistance(node, target):
            if not node:
                return -1
            if node.data == target:
                return 0

            left_distance = nodeDistance(node.left, target)
            right_distance = nodeDistance(node.right, target)

            if left_distance >= 0:
                return left_distance + 1
            if right_distance >= 0:
                return right_distance + 1

            return -1
        
        # lca is lowestCommonAncestor

        def lowestCommonAncestor(node, a, b):
            if not node:
                return None
            if node.data == a or node.data == b:
                return node

            # left_lca is Left lowestCommonAncestor
            # right_lca is Right lowestCommonAncestor
            
            left_lca = lowestCommonAncestor(node.left, a, b)
            right_lca = lowestCommonAncestor(node.right, a, b)

            if left_lca and right_lca:
                return node
            return left_lca if left_lca else right_lca

        # lca_node is lowestCommonAncestor Node
        lca_node = lowestCommonAncestor(root, a, b)
        return nodeDistance(lca_node, a) + nodeDistance(lca_node, b)
