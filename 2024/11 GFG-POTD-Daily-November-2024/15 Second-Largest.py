# User function Template for python3

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        maxi = arr[0]
        maxiSum = 0
        for i in range(len(arr)):
            if arr[i] > maxi:
                maxi = arr[i]
        for i in range(len(arr)):
            if arr[i] > maxiSum and arr[i] != maxi:
                maxiSum = arr[i]
        return -1 if maxiSum == 0 else maxiSum
