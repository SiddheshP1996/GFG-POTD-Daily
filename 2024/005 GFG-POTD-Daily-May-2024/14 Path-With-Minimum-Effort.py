# User function Template for python3

from typing import List
from heapq import heappop, heappush

class Solution:
    def MinimumEffort(self, rows : int, columinimums : int, heights : List[List[int]]) -> int:
        # Code here
        height = len(heights)
        width = len(heights[0])
        result_dp = [[float('inf') for _ in range(width)] for _ in range(height)]
        result_dp[0][0] = 0
        q = [(0, 0, 0, )]
        while q:
            maximumx, rowElement, columnElement = heappop(q)
            for dimensionX, dimensionY in [(-1, 0, ), (1, 0, ), (0, -1, ), (0, 1, )]:
                newX, newY = rowElement + dimensionX, columnElement + dimensionY
                if not(0 <= newX < width and 0 <= newY < height):
                    continue
                minimum = min(result_dp[newY][newX], max(maximumx, abs(heights[columnElement][rowElement] - heights[newY][newX])))
                if minimum < result_dp[newY][newX]:
                    result_dp[newY][newX] = minimum
                    heappush(q, ((minimum, newX, newY, )))
        return result_dp[-1][-1]
