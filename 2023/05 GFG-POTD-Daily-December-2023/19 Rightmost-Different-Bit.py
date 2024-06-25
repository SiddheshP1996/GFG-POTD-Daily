# User function Template for python3
import math


class Solution:

    # Function to find the first position with different bits.
    def posOfRightMostDiffBit(self, m, n):
        # Your code here
        xorBinaryResult = m ^ n
        if xorBinaryResult == 0:
            return -1
        return int(math.log2(xorBinaryResult & -xorBinaryResult) + 1)
