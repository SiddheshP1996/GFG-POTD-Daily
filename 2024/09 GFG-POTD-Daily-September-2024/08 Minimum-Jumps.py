# User function Template for python3

class Solution:
    def minJumps(self, arr):
        # Code here
        arrayLength = len(arr)
        x = y = z = 0

        for i in range(arrayLength - 1):
            x = max(x, arr[i] + i)
            if i == y:
                y = x
                z += 1

        if y >= arrayLength - 1:
            return z
        return -1
