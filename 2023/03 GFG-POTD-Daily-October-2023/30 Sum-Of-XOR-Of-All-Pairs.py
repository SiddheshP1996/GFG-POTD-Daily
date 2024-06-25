# User function Template for python3

import math


class Solution:
    def sumXOR(self, arr, n):
        # Complete the function
        summation = 0
        high = int(math.log2(max(arr)) + 1)
        for i in range(high):
            setBit = 0
            for j in arr:
                if j & (1 << i):
                    setBit += 1
            summation += (setBit * (n - setBit) * (1 << i))
        return summation
