# User function Template for python3

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self, root, k):
        # your code here
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            l.append(root.data)
            inorder(root.right)

        l = []
        inorder(root)
        return l[-k]
