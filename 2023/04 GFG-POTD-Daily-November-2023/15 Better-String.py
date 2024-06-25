# User function Template for python3

class Solution:
    def countDistance(self, s):
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        lastOccurence = {}
        for i in range(1, len(s) + 1):
            dp[i] = 2 * dp[i - 1]
            if s[i - 1] in lastOccurence:
                dp[i] -= dp[lastOccurence[s[i - 1]] - 1]

            lastOccurence[s[i - 1]] = i
        return dp[len(s)]

    def betterString(self, str1, str2):
        # Code here
        if self.countDistance(str1) >= self.countDistance(str2):
            return str1
        else:
            return str2
        