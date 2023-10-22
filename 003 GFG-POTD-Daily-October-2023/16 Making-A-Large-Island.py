# User function Template for python3

from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        # Code here
        def dfs(row, col, island_id):
            if 0 <= row < n and 0 <= col < n and grid[row][col] == 1:
                grid[row][col] = island_id
                size = 1
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    size += dfs(row + dr, col + dc, island_id)
                return size
            return 0

        n = len(grid)
        island_sizes = {}  # Store the size of each island using island_id as the key
        island_id = 2  # Start island_id from 2 (1 is used for water, 0 for unvisited land)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, island_id)
                    island_sizes[island_id] = size
                    island_id += 1

        max_island_size = max(island_sizes.values()) if island_sizes else 0

        # Try changing each 0 to 1 and see if it can connect two islands
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    adjacent_islands = set()
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        ni, nj = i + dr, j + dc
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            adjacent_islands.add(grid[ni][nj])
                    new_island_size = 1 + sum(island_sizes[adj_island] for adj_island in adjacent_islands)
                    max_island_size = max(max_island_size, new_island_size)

        return max_island_size
    