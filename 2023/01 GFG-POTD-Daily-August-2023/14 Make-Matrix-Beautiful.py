# User function Template for python3

class Solution:
    def findMinOpeartion(self, matrix, n):
        # Code here
        max_element_sum = 0
        sum = 0

        for i in range(n):
            row = 0  # row sum
            column = 0  # col sum

            for j in range(n):
                row += matrix[i][j]
                column += matrix[j][i]

            sum += row
            max_element_sum = max((max_element_sum, row, column))

        return n * max_element_sum - sum