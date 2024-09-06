# User function Template for python3

class Solution:
    # Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        # Your code here
        result, current = arr[0], 0
        for item in arr:
            current += item
            result = max(current, result)
            current = max(current, 0)
            
        return result
