# User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        # Code here
        n = len(nums)
        
        if n == 1:
            return [1]
            
        leftProduct = [1] * n
        rightProduct = [1] * n
        finalProduct = [0] * n
        
        for i in range(1, n):
            leftProduct[i] = nums[i - 1] * leftProduct[i - 1]
            
        for i in range(n - 2, -1, -1):
            rightProduct[i] = nums[i + 1] * rightProduct[i + 1]
        
        for i in range(n):
            finalProduct[i] = leftProduct[i] * rightProduct[i]
            
        return finalProduct
