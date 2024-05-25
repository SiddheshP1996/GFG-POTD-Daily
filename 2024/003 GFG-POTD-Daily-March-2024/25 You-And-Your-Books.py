# User function Template for python3

class Solution:
    # Your task is to complete this function
    # Function should return an integer
    # a - list/array containing height of stack's respectively
    def max_Books(self, n, k, arr):
        # code here
        currentItem, result = 0, 0
        for item in arr:
            if item <= k:
                currentItem += item
            else:
                result = max(result, currentItem)
                currentItem = 0
        return max(result, currentItem)
