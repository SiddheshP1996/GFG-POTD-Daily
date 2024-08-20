# User function Template for python3

class Solution:
    def minTime(self, root, target):
        # Code here
        result=[0]*1
        def functionOne(root):
            if root == None:
                return -1
            
            return max(1 + functionOne(root.left), 1 + functionOne(root.right))
        
        def functionTwo(root):
            if root == None:
                return -1
            
            if root.data == target:
                x = functionOne(root)
                result[0] = max(result[0], x)
                return 1
            
            left = functionTwo(root.left)
            
            if left != -1:
                x = functionOne(root.right)
                result[0] = max(result[0], x + left + 1)
                return left + 1
            
            right = functionTwo(root.right)
            
            if right != -1:
                x = functionOne(root.left)
                result[0] = max(result[0], x + right + 1)
                return right + 1
            
            return -1
        
        functionTwo(root)
        return result[0]
