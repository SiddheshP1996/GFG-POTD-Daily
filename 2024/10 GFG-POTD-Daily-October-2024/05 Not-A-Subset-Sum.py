# User function Template for python3

class Solution:
    def findSmallest(self, arr):
        # Code here
        result = 1
        for i in range(len(arr)):
            if arr[i] <= result:
                result += arr[i]
        return result
