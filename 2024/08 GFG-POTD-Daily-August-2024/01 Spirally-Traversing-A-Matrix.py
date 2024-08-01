# User function Template for python3

class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix):
        # Code here
        result = []
        while matrix:
            result += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return result
