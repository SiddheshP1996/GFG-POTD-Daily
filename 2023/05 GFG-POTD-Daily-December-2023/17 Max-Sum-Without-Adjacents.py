# User function Template for python3

class Solution:

    def findMaxSum(self, arr, n):
        # Code here
        dp = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], arr[i] + dp[i + 2])

        return dp[0]
