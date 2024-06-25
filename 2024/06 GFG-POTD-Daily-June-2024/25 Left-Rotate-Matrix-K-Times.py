# User function Template for python3

class Solution:
    def rotateMatrix(self, k, mat):
        # Code here
        n = len(mat)
        rotatedMatrix = []
        for row in mat:
              effectiveK = k % len(row)
              rotatedRow = row[effectiveK:] + row[:effectiveK]
              rotatedMatrix.append(rotatedRow)
    
        return rotatedMatrix
