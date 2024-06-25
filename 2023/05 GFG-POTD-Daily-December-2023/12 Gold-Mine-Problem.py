# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        # Code here
        # Create a 2D table to store the maximum gold collected at each cell
        dp = [[0] * m for _ in range(n)]

        # Fill the last column of the dp table
        for i in range(n):
            dp[i][m - 1] = M[i][m - 1]

        # Traverse the mine column-wise from right-side-element to left-side-element
        for j in range(m - 2, -1, -1):
            for i in range(n):
                # Consider all possible moves and find the maximum
                rightElement = dp[i][j + 1]
                rightUpElement = dp[i - 1][j + 1] if i > 0 else 0
                rightDownElement = dp[i + 1][j + 1] if i < n - 1 else 0

                dp[i][j] = M[i][j] + max(rightElement, rightUpElement, rightDownElement)

        # Find the maximum value in the first column (starting column)
        maxAmtGold = 0
        for i in range(n):
            maxAmtGold = max(maxAmtGold, dp[i][0])

        return maxAmtGold
