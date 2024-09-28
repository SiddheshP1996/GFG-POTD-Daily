# User function Template for python3

class Solution:
    def minimizeCost(self, k, arr):
        # Code here
        result = [float('inf')] * len(arr)
        result[0] = 0
        
        for i in range(1, len(arr)):
            for j in range(max(0, i - k), i):
                result[i] = min(result[i], result[j] + abs(arr[i] - arr[j]))
        return result[len(arr) - 1]
