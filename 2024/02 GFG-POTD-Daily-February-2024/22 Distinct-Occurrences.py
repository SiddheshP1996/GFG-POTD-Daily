# Your task is to complete this function
# Function should return Integer

class Solution:
    def sequenceCount(self,s, t):
        # Code here
        mod = ((10 ** 9) + 7)
        dp = {}
        def executeCount(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j == len(t):
                return 1
            if i >= len(s) or j >= len(t):
                return 0
            if s[i] == t[j]:
                dp[(i, j)] = executeCount(i + 1, j + 1) + executeCount(i + 1, j)
            else:
                dp[(i, j)] = executeCount(i + 1, j)
            return dp[(i, j)] % mod
        return executeCount(0, 0) % mod
