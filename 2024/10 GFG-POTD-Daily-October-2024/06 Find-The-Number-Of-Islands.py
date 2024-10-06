# User function Template for python3

class Solution:
    def numIslands(self, grid):
        # Code here
        if not grid:
            return 0
    
        n, m = len(grid), len(grid[0])    
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
        def dfsIterative(x, y):
            stack = [(x, y)]
            while stack:
                cx, cy = stack.pop()
                if cx < 0 or cx >= n or cy < 0 or cy >= m or grid[cx][cy] == 0:
                    continue
    
                grid[cx][cy] = 0
                for dx, dy in directions:
                    stack.append((cx + dx, cy + dy))
    
        islandCount = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    islandCount += 1
                    dfsIterative(i, j)
    
        return islandCount
