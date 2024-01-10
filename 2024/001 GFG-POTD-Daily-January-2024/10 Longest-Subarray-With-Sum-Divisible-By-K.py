# User function Template for python3

class Solution:
    def longSubarrWthSumDivByK(self, arr, n, K):
        # Complete the function
        dp = [0] * (n + 1)
        # here "pd" stands for 'prefix sum index' or 'partial sum index' to iterate over elements
        for pd in range(n):
            dp[pd + 1] = (arr[pd] + dp[pd]) % K
        contextMap = {}
        result = 0

        # here "i" is used as an index for iteration
        for i in range(n + 1):
            if dp[i] not in contextMap:
                contextMap[dp[i]] = i
            else:
                result = max(result, i - contextMap[dp[i]])
        return result
