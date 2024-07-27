# User function Template for python3

class Solution:
    def countMin(self, str):
        # Code here
        if str == str[::-1]:
            return 0

        n = len(str)
        dp = [[0 for i in range(n)] for j in range(n)]
        
        for i in range(n - 1):
            if str[i] == str[i + 1]:
                dp[i][i + 1] = 0
            else:
                dp[i][i + 1] = 1
                
        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                if str[i] == str[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
                    
        return dp[0][n - 1]
