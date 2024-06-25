# User function Template for python3

from typing import List

class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        # Code here
        if n <= 1:
            return 0
        
        left = [0] * n
        minimumPrice = price[0]
        
        for loss in range(1, n):
            minimumPrice = min(minimumPrice, price[loss])
            left[loss] = max(left[loss - 1], price[loss] - minimumPrice)
            
        maximumPrice = price[-1]
        resultPrice = left[-1]
        
        for profit in range(n - 2, 0, -1):
            maximumPrice = max(maximumPrice, price[profit])
            resultPrice = max(resultPrice, left[profit - 1] + maximumPrice - price[profit])
        return resultPrice
