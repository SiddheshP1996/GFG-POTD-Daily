# User function Template for python3

from typing import List
from collections import deque

class Solution:
    def findShortestPath(self, mat : List[List[int]]) -> int:
        # Code here
        if not mat or not mat[0]:
            return -1
        
        matrix_n, matrix_m = len(mat), len(mat[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  
        def is_blocked(x, y):
            if mat[x][y] == 0:
                return True
            for dx, dy in directions:
                matrix_nx, matrix_ny = x + dx, y + dy
                if 0 <= matrix_nx < matrix_n and 0 <= matrix_ny < matrix_m and mat[matrix_nx][matrix_ny] == 0:
                    return True
            return False
        
        queue = deque([(i, 0, 1) for i in range(matrix_n) if not is_blocked(i, 0)])
        matrix_visited = [[False for _ in range(matrix_m)] for _ in range(matrix_n)]  # Visited matrix
        
        while queue:
            x, y, dist = queue.popleft()
            if y == matrix_m - 1:
                return dist
            for dx, dy in directions:
                matrix_nx, matrix_ny = x + dx, y + dy
                if 0 <= matrix_nx < matrix_n and 0 <= matrix_ny < matrix_m and not matrix_visited[matrix_nx][matrix_ny] and not is_blocked(matrix_nx, matrix_ny):
                    matrix_visited[matrix_nx][matrix_ny] = True  
                    queue.append((matrix_nx, matrix_ny, dist + 1))
        
        return -1
