# User function Template for python3

from typing import List


class Solution:
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        # Code here
        result = max(max(mat[0]), max([mat[i][0] for i in range(n)]))

        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j]:
                    matrixMin = min(mat[i - 1][j - 1], mat[i - 1][j], mat[i][j - 1])
                    mat[i][j] = 1 + matrixMin
                    result = max(result, mat[i][j])
        
        return result
