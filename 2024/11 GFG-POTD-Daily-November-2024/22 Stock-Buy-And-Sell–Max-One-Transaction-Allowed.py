# User function Template for python3

class Solution:
    def maximumProfit(self, prices):
        # Code here
        minPrice = float('inf')
        maxProfit = 0

        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)

        return maxProfit
