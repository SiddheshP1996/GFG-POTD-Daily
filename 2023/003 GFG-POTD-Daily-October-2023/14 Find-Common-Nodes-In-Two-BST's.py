# User function Template for python3


class Solution:

    # Function to find the nodes that are common in both BST.
    def findCommon(self, root1, root2):
        # code here
        lst1 = self.TreeToList(root1)
        lst2 = self.TreeToList(root2)
        lst3 = list(set(lst1) & set(lst2))
        lst3.sort()
        return lst3

    def TreeToList(self, root):
        def in_order_traversal(node):
            if node is not None:
                in_order_traversal(node.left)
                sorted_list.append(node.data)
                in_order_traversal(node.right)

        sorted_list = []
        in_order_traversal(root)
        return sorted_list
