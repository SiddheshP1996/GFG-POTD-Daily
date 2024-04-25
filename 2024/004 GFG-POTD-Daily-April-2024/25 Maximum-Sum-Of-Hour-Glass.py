# User function Template for python3

class Solution:
    def hourGlass(self, i, j, mat):
        return (mat[i][j] + mat[i][j + 1] + mat[i][j + 2]
                + mat[i + 1][j + 1] 
                + mat[i + 2][j] + mat[i + 2][j + 1] + mat[i + 2][j + 2])
            
    def findMaxSum(self, n, m, mat):
        # Code here
        if n < 3:
            return -1
        result =- float("inf")
        for i in range(n - 2):
            for j in range(m - 2):
                currentHourGlass = self.hourGlass(i, j, mat)
                result = max(result, currentHourGlass)
        return result
