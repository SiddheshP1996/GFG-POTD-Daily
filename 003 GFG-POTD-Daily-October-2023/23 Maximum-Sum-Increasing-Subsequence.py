# User function Template for python3
class Solution:
    def maxSumIS(self, Arr, n):
        # code here
        # Initialize the dp array
        dp = [x for x in Arr]

        # Loop through each element in the array
        for i in range(1, n):
            for j in range(i):
                # If an increasing subsequence can be formed
                if Arr[i] > Arr[j]:
                    dp[i] = max(dp[i], dp[j] + Arr[i])

        # The maximum sum of increasing subsequence is the maximum value in dp
        return max(dp)
