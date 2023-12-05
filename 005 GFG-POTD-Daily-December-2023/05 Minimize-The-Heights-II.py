# User function Template for python3


class Solution:
    def getMinDiff(self, arr, n, k):
        # Code here
        arr.sort()
        result = arr[-1] - arr[0]

        for i in range(1, len(arr)):
            if arr[i] - k < 0:
                continue
            else:
                maximum = max(arr[i - 1] + k, arr[-1] - k)
                minimum = min(arr[i] - k, arr[0] + k)
                result = min(result, maximum - minimum)

        return result
