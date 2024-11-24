# User function Template for python3

class Solution:
    # Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        # Your code here
        result = arrSum = -1e9
        for a in arr:
            arrSum = max(a, arrSum + a)
            result = max(result, arrSum)

        return result
