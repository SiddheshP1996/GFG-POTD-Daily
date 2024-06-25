# User function Template for python3

class Solution:

    # Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):

        # code here
        def lcsLength():
            L = [[0] * (n + 1) for _ in range(m + 1)]

            for i in range(m + 1):
                for j in range(n + 1):
                    if i == 0 or j == 0:
                        L[i][j] = 0
                    elif X[i - 1] == Y[j - 1]:
                        L[i][j] = L[i - 1][j - 1] + 1
                    else:
                        L[i][j] = max(L[i - 1][j], L[i][j - 1])

            return L[m][n]

        return m + n - lcsLength()
    