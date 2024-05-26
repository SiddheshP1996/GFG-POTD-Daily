# User function Template for python3

class Solution:
    def findMinCost(self, x, y, costX, costY):
        # Code here
        n, m = len(x), len(y)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                dp[i + 1][j + 1] = 1 + dp[i][j] if x[i] == y[j] else max(dp[i + 1][j], dp[i][j + 1])
        
        return costX * (n - dp[-1][-1]) + costY * (m - dp[-1][-1])
