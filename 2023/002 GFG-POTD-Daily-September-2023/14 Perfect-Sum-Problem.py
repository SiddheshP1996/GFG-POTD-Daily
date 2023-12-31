# User function Template for python3


class Solution:
    def perfectSum(self, arr, n, sum):
        # code here
        dp = [1] + [0] * sum
        MOD = 10 ** 9 + 7
        for a in arr:
            for i in range(sum, a - 1, -1):
                dp[i] = (dp[i] + dp[i - a]) % MOD
        return dp[sum]
