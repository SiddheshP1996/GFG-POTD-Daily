# User function Template for python3

from typing import List


class Solution:
    def isPossible(self, N : int, coins : List[int]) -> bool:
        # Code here
        def programHelper(i, sumOfCoins):
            if sumOfCoins > 0 and (sumOfCoins % 20 == 0 or sumOfCoins % 24 == 0 or sumOfCoins == 2024):
                return True
            if i >= N:
                return False
            return programHelper(i + 1, sumOfCoins + coins[i]) or programHelper(i + 1, sumOfCoins)
        return programHelper(0, 0)
