# User function Template for python3

from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        # Code here
        priceArray = []
        for i in range(n):
            priceArray.append([price[i], i+1])
        priceArray.sort()
        result = 0
        for i in range(n):
            if priceArray[i][0] * priceArray[i][1] <= k:
                result += priceArray[i][1]
                k -= priceArray[i][0] * priceArray[i][1]
            else:
                result += k // priceArray[i][0]
                break
        return result
