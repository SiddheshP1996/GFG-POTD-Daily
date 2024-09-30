# User function Template for python3

class Solution:
    def inorderTraversal(self, rootNode, lists):
        if rootNode is not None:
            self.inorderTraversal(rootNode.left, lists)
            lists.append(rootNode.data)
            self.inorderTraversal(rootNode.right, lists)
        return lists
    
    def merge(self, root1, root2):
        # Code here
        list1 = self.inorderTraversal(root1, [])
        list2 = self.inorderTraversal(root2, [])
        lists = list1 + list2
        lists.sort()
        return lists
