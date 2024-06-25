# User function Template for python3

class Solution:
    
    def getCofactor(self, matrix, row, col, n):
        cofactorOfMatrix = []
        for i in range(n):
            if i != row:
                cofactorInRow = []
                for j in range(n):
                    if j != col:
                        cofactorInRow.append(matrix[i][j])
                cofactorOfMatrix.append(cofactorInRow)
        return cofactorOfMatrix
    
    # Function for finding determinant of matrix.
    def determinantOfMatrix(self, matrix, n):
        # Code here
        if n == 1:
            return matrix[0][0]

        det = 0

        for i in range(n):
            cofactorOfMatrix = self.getCofactor(matrix, 0, i, n)
            
            det += matrix[0][i] * ((-1) ** i) * self.determinantOfMatrix(cofactorOfMatrix, n - 1)

        return det
