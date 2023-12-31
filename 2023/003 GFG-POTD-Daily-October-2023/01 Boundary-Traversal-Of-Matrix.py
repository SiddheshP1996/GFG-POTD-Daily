# User function Template for python3

class Solution:

    # Function to return list of integers that form the boundary
    # traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self, matrix, n, m):
        # code here
        result = []
        if n == 1:
            result.extend(matrix[0])
        elif m == 1:
            for i in range(n):
                result.append(matrix[i][0])
        else:
            # Traverse the top row
            for i in range(m):
                result.append(matrix[0][i])

            # Traverse the rightmost column
            for i in range(1, n):
                result.append(matrix[i][m - 1])

            # Traverse the bottom row (if there is one)
            if n > 1:
                for i in range(m - 2, -1, -1):
                    result.append(matrix[n - 1][i])

            # Traverse the leftmost column (if there is one)
            if m > 1:
                for i in range(n - 2, 0, -1):
                    result.append(matrix[i][0])

        return result
