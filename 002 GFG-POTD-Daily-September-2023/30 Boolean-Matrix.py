# User function Template for python3

from copy import deepcopy


# Function to modify the matrix such that if a matrix cell matrix[i][j]
# is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    # code here
    # Create a deep copy of the input matrix
    mat = deepcopy(matrix)
    rows, cols = len(matrix), len(matrix[0])

    # Lists to keep track of rows and columns to be modified

    rowsToModify = [False] * rows
    colsToModify = [False] * cols

    # Traverse the matrix and mark rows and columns to be modified

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                rowsToModify[i] = True
                colsToModify[j] = True

    # Modify the matrix based on the marked rows and columns

    for i in range(rows):
        for j in range(cols):
            if rowsToModify[i] or colsToModify[j]:
                matrix[i][j] = 1
