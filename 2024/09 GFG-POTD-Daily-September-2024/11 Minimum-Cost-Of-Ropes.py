# User function Template for python3

from typing import List
from heapq import heappop, heappush, heapify

class Solution:
    # Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr: List[int]) -> int:
        # Code here
        cost = 0
        h = arr
        heapify(h)
        
        while len(h) > 1:
            p1 = heappop(h)
            p2 = heappop(h)
            cost += p1 + p2
            heappush(h, p1 + p2)
        
        return cost
