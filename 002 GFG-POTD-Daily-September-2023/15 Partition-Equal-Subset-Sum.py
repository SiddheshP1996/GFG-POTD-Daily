# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here
        # check the whole sum
        s = sum(arr)
        if s % 2 == 1:
            return 0
        else:
            target = s // 2

            # initialization for dynamic programming
            dp = [[0] * (target + 1) for _ in range(N + 1)]
            dp[0] = [1] + [0] * target

            # recursive scheme, stop if target is achieved
            i = 1
            while i < N:
                for j in range(target + 1):
                    if j >= arr[i - 1]:
                        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]
                    else:
                        dp[i][j] = dp[i - 1][j]
                if dp[i][target] > 0:
                    return 1
                i = i + 1

            return 0
