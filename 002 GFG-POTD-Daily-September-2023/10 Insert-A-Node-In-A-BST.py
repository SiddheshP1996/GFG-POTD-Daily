# User function Template for python3

class Solution:
    # Function to insert a node in a BST.
    def insert(self, root, Key):
        # code here
        if root == None:
            return Node(Key)

        if root.data == Key:
            return root

        if root.data > Key:

            if root.left:
                self.insert(root.left, Key)

            else:
                root.left = Node(Key)
                return root

        if root.data < Key:

            if root.right:
                self.insert(root.right, Key)

            else:
                root.right = Node(Key)
                return root