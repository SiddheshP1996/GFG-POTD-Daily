# User function Template for python3


class Solution:

    def checkTriplet(self, arr, n):
        # code here
        """
        Create a dictionary to store the square of each element as keys
        and the corresponding original element as values.
        """
        squareMap = {i * i: i for i in arr}

        # Iterate through the square_map to find triplets with the sum of squares.
        for square1 in squareMap:
            for square2 in squareMap:
                # Calculate the sum of two squared values.
                sumOfSquares = square1 + square2

                # Check if the sum exists in the square_map, indicating the presence of a triplet.
                if sumOfSquares in squareMap:
                    return True

        # If no triplet is found, return False.
        return False
