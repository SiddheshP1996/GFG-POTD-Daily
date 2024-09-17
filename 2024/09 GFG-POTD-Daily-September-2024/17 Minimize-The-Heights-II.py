# User function Template for python3

class Solution:
    def getMinDiff(self, arr, k):
        # Code here
        n = len(arr)
        if n == 1:
            return 0

        arr.sort()

        result = arr[-1] - arr[0]

        for i in range(1, n):
            if arr[i] - k < 0:
                continue

            highest = max(arr[i - 1] + k, arr[-1] - k)
            lowest = min(arr[0] + k, arr[i] - k)

            result = min(result, highest - lowest)

        return result
