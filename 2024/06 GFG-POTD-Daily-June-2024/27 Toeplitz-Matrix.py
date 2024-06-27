# You are required to complete this method
# Return True/False or 1/0

def isToeplitz(mat):
    # Code here
    n = len(mat)
    m = len(mat[0])
    def isToeplitzValid(x, y):
        return x < n and y < m
    for i in range(0, n):
        for j in range(0, m):
            if isToeplitzValid(i + 1, j + 1) and mat[i][j] != mat[i + 1][j + 1]:
                return False
    return True
