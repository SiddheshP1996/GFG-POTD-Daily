# User function Template for python3

from typing import List


class Solution:
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        # Code here
        mod = ((10 ** 9) + 7)
    
        totalSum = sum(arr)
        
        if (totalSum - d) % 2 != 0 or totalSum < d:
            return 0
        
        partitionCount = (totalSum - d) // 2
    
        dp = [0] * (partitionCount + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(partitionCount, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % mod
        
        return dp[partitionCount]
