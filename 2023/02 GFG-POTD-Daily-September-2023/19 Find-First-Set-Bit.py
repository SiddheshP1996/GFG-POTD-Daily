# User function Template for python3

class Solution:

    # Function to find position of first set bit in the given number.
    def getFirstSetBit(self, n):
        # Your code here
        result = []
        while n != 0:
            remainder = n % 2
            n = n // 2
            result.append(remainder)
        for i in range(0, len(result)):
            if result[i] == 1:
                return i + 1
        return 0
