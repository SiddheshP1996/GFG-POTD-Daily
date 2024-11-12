# User function Template for python3

class Solution:
    def canAttend(self, arr):
        # Your Code Here
        arr.sort()
        for i in range(1, len(arr)):
            if arr[i][0] < arr[i - 1][-1]:
                return 0
        return 1
