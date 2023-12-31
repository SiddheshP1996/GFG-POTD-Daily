# User function Template for python3

# Solution No 1

class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def check(self, rootl, rootr):
        if not rootl and not rootr:
            return True

        if not rootl or not rootr:
            return False

        if rootl.data != rootr.data:
            return False

        return self.check(rootl.left, rootr.right) and self.check(rootl.right, rootr.left)

    def isSymmetric(self, root):
        # Your Code Here
        if not root:
            return True

        return self.check(root.left, root.right)


# Solution No 2
"""        
class Solution:
    def isSymmetric(self, root):
        def fun(node1, node2):
            return True if not node1 and not node2 else (False if ((not node1 or not node2) or (node1.data!=node2.data)) else (fun(node1.left, node2.right) and fun(node1.right, node2.left)))
        return fun(root.left, root.right) if root else True
"""
