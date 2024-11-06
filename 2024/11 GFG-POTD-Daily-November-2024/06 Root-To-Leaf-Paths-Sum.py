# Your task is to complete this function
# Function should return max sum level in the tree
class Solution:
    def dfs(self, root, currentSum, result):
        if root == None:
            return
        
        currentSum = currentSum * 10 + root.data
        if root.left == None and root.right == None:
            result[0] += currentSum
        else:
            self.dfs(root.left, currentSum, result)
            self.dfs(root.right, currentSum, result)
            
    def treePathSum(self, root):
        # Code here
        result = [0]
        self.dfs(root, 0, result)
        return result[0]
