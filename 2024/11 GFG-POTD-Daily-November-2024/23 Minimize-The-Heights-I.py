# User function Template for python3

class Solution:
    def getMinDiff(self, k, arr):
        # Code here
        arr.sort()
        result = arr[-1] - arr[0]
        
        for i in range(1, len(arr)):
            minHeight = min(arr[0] + k, arr[i] - k)
            maxHeight = max(arr[i - 1] + k, arr[-1] - k)
            result = min(result, maxHeight - minHeight)
        
        return result
