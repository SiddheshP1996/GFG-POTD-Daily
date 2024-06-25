# User function Template for python3

class Solution:

    def LCSof3(self, A, B, C, n1, n2, n3):
        # Code here
        dp = [[[0 for num in range(n3 + 1)] for num in range(n2 + 1)] for num in range(n1 + 1)]
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                for k in range(n3 - 1, -1, -1):
                    if A[i] == B[j] == C[k]:
                        dp[i][j][k] = 1 + dp[i + 1][j + 1][k + 1]
                    else:
                        dp[i][j][k] = max(dp[i + 1][j][k], max(dp[i][j + 1][k], dp[i][j][k + 1]))
        return dp[0][0][0]
