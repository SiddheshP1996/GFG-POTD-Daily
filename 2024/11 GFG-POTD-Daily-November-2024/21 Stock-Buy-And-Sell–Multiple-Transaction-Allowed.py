# User function Template for python3

from typing import List

class Solution:
    def maximumProfit(self, prices) -> int:
        # Code here
        n = len(prices)
        maxPrice = 0
        left, right = 0, 0
        while right < n - 1:
            if prices[right] <= prices[right + 1]:
                profit = prices[right + 1] - prices[left]
                maxPrice += profit
            right += 1
            left += 1
        return maxPrice
