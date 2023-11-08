# User function Template for python3

class Solution:

    # Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix):
        # code here
        snakeDirection = []
        for i in range(len(matrix)):
            # Check if the row number is even using bitwise AND
            if i & 1 == 0:
                # If even row, extend the snake list with the entire row
                snakeDirection.extend(matrix[i])
            else:
                # If odd row, extend the snake list with the reversed row
                snakeDirection.extend(reversed(matrix[i]))
        return snakeDirection
    