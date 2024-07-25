# User function Template for python3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        # Code here
        if not nums:
            return None
        
        middleNode = len(nums) // 2
        rootNode = TreeNode(nums[middleNode])
        
        rootNode.left = self.sortedArrayToBST(nums[:middleNode])  
        rootNode.right = self.sortedArrayToBST(nums[middleNode + 1:])  
        
        return rootNode
