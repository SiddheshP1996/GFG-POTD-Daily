# User function Template for python3

class Solution:
    def rearrange(self, arr):
        # Code here
        result = [-1] * len(arr)
        for value in arr:
            if 0 <= value < len(arr):
                result[value] = value
        return result
