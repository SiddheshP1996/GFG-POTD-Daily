# User function Template for python3

class Solution:
    # Your task is to complete this function
    # Function should return True/False or 1/0
    def check(self, root):
        # Code here
        # Set to store levels of leaf nodes
        tree_leaf_levels = set()
       
        # Helper function to traverse tree and record leaf levels
        def tree_traverse(node, level):
            if not node:
                return
            if not node.left and not node.right:
                tree_leaf_levels.add(level)
            tree_traverse(node.left, level + 1)
            tree_traverse(node.right, level + 1)
       
        # Start traversal from root at level 0
        tree_traverse(root, 0)
       
        # If all leaf nodes are at the same level, return True, else False
        return len(tree_leaf_levels) == 1
