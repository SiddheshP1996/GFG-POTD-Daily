# User function Template for python3

class Solution:
    def findSingle(self, n, arr):
        # Code here
        result = 0
        for i in arr:
            result ^= i
        return result
