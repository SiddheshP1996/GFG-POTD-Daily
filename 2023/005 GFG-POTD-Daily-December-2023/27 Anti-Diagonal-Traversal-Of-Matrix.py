# User function Template for python3

class Solution:
    def antiDiagonalPattern(self,matrix):
        # Code here
        n = len(matrix)
        result = []

        for i in range(n):
            k = 0
            for j in range(i, -1, -1):
                result.append(matrix[k][j])
                k += 1

        for i in range(1, n):
            k = i
            for j in range(n - 1, i - 1, -1):
                result.append(matrix[k][j])
                k += 1

        return result
