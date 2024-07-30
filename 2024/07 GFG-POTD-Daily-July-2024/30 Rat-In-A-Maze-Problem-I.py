# User function Template for python3
from typing import List

class Solution:
    matrixDir = [
        [-1, 0, "U"],
        [1, 0, "D"],
        [0, -1, "L"],
        [0, 1, "R"]
    ]

    def dfs(self, m, x, y, result, currentIndex):
        rows, columns = len(m), len(m[0])
        if x == rows - 1 and y == columns - 1:
            result.append(currentIndex)
            return
        
        m[x][y] = 2
        for dx, dy, symbol in self.matrixDir:
            newX, newY = x + dx, y + dy
            if 0 <= newX < rows and 0 <= newY < columns and m[newX][newY] == 1:
                self.dfs(m, newX, newY, result, currentIndex + symbol)
                
        m[x][y] = 1

    def findPath(self, m: List[List[int]]) -> List[str]:
        # Code here
        result = []
        if m[0][0]:
            self.dfs(m, 0, 0, result, "")
        return result
