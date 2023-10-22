# User function Template for python3
class Solution:
    # Return True if the given trees are isomotphic. Else return False.
    def isIsomorphic(self, root1, root2):
        # code here.
        if root1 is None and root2 is None:
            return True

        if root1 is not None and root2 is not None:
            if root1.data == root2.data:
                if self.isIsomorphic(root1.left, root2.right) and self.isIsomorphic(root1.right, root2.left):
                    return True
                elif self.isIsomorphic(root1.left, root2.left) and self.isIsomorphic(root1.right, root2.right):
                    return True
        return False