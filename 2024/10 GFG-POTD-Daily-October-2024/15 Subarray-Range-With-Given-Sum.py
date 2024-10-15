# User function Template for python3

from collections import defaultdict

class Solution:
    # Complete this fuction
    # Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self, arr, tar):
        # Your code here
        count = defaultdict(int, {0: 1})
        
        sumation, result = 0, 0
        for element in arr:
            sumation += element
            result += count[sumation - tar]
            count[sumation] += 1
        return result
