# User function Template for python3

class Solution:
    def largestSubsquare(self, n, a):
        # Code here
        n = len(a)
        dp = [[(0, 0)] * (n + 1) for num in range(n + 1)]
        
        for r in range(n):
            for c in range(n):
                if a[r][c] == 'X':
                    dp[r + 1][c + 1] = (dp[r][c + 1][0] + 1, dp[r + 1][c][1] + 1)

        result = 0
        for r in range(1, n + 1):
            for c in range(1, n + 1):
                d = min(dp[r][c])
                while d > result:
                    left = c - d + 1
                    top = r - d + 1
                    if dp[r][left][0] >= d and dp[top][c][1] >= d:
                        result = d
                        break
                    d -= 1
        return result
