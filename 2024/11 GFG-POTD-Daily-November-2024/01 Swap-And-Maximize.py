# User function Template for python3

class Solution:
    def maxSum(self, arr):
        # Code here
        arr.sort()
        resultSum = 0
        for i in range(len(arr) // 2):
            resultSum += arr[len(arr) - i - 1] - arr[i]
            resultSum += arr[len(arr) - i - 1] - arr[i + 1]
        resultSum += arr[len(arr) // 2] - arr[0]
        return resultSum
