# User function Template for python3

class Solution:
    def findCoverage(self, matrix):
        # Code here
        countOne=0
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if(i - 1 >= 0 and matrix[i - 1][j] == 1):
                        countOne += 1
                    if(i + 1 < n and matrix[i + 1][j] == 1):
                        countOne += 1
                    if(j - 1 >= 0 and matrix[i][j - 1] == 1):
                        countOne += 1
                    if(j + 1 < m and matrix[i][j + 1] == 1):
                        countOne += 1
        return countOne
