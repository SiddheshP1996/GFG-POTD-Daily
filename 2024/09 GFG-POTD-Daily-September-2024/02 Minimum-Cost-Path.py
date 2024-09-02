# User function Template for python3

from heapq import heappush, heappop

class Solution:
    # Function to return the minimum cost to react at bottom
    # right cell from top left cell.
    def minimumCostPath(self, grid):
        # Code here
        INF = float('inf')
        m, n = len(grid), len(grid[0])
        seen = set()
        q = [(grid[0][0], (0, 0))]
        while q:
            cost0, (rowCost, columnCost) = heappop(q)
            if (rowCost, columnCost) in seen:
                continue
            
            if rowCost == m - 1 and columnCost == n - 1:
                return cost0
            
            seen.add((rowCost, columnCost))
            for newRow, newColumn in [(rowCost + 1, columnCost), (rowCost - 1, columnCost),\
                (rowCost, columnCost + 1), (rowCost, columnCost - 1)]:
                if 0 <= newRow < m and 0 <= newColumn < n:
                    heappush(q, (cost0 + grid[newRow][newColumn], (newRow, newColumn)))
        return -1
