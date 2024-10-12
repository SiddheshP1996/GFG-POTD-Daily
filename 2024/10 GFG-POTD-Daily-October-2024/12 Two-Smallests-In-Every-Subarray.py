# User function Template for python3

class Solution:
    def pairWithMaxSum(self, arr):
        # Code here
        result = 0
        for i in range(1, len(arr)):
            result = max(result, arr[i] + arr[i - 1])
        return result if result else -1
