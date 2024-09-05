# User function Template for python3
class Solution:
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        # Code here
        add = n * (n + 1) / 2
        return int(add - sum(arr))
