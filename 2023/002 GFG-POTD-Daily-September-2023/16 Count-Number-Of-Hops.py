# User function Template for python3

class Solution:
    # Function to count the number of ways in which frog can reach the top.
    def countWays(self, n):

        # code here
        mod = 10 ** 9 + 7
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        coins = (1, 2, 3)

        for i in range(n + 1):
            for j in coins:
                newPosition = i + j
                if newPosition <= n:
                    dp[newPosition] = (dp[newPosition] + dp[i]) % mod
        return dp[n]