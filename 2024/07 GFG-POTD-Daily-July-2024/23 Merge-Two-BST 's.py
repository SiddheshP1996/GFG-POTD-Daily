# User function Template for python3

class Solution:
    def merge(self, root1, root2):
        # Code here
        def mergeInOrder(root ,result):
            if root == None:
                return 
        
            mergeInOrder(root.left, result)
            result.append(root.data)
            mergeInOrder(root.right, result)
        
        result = []
        
        mergeInOrder(root1, result)
        mergeInOrder(root2, result)
        result.sort()
        
        return result
