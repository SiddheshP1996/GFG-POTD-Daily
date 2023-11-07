# User function Template for python3


class Solution:

    # Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self, matrix, n):
        # code here
        upperTriangleElements = 0
        lowerTriangleElements = 0

        for i in range(n):
            for j in range(i, n):
                upperTriangleElements += matrix[i][j]

            for j in range(0, i + 1):
                lowerTriangleElements += matrix[i][j]

        results = [upperTriangleElements, lowerTriangleElements]

        return results
    