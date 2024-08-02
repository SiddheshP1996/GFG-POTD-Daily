# User function Template for python3

class Solution:
    def editDistance(self, str1, str3):
        # Code here
        stringOneLength, stringThreeLength = len(str1), len(str3)
        dp = [[0 for _ in range(stringThreeLength + 1)] for _ in range(stringOneLength + 1)]

        for i in range(stringThreeLength):
            dp[0][i + 1] = i + 1

        for i in range(stringOneLength):
            dp[i + 1][0] = i + 1

        for i in range(stringOneLength):
            for j in range(stringThreeLength):
                if str1[i] == str3[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1

        return dp[-1][-1]
