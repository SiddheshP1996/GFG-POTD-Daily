# User function Template for python3

class Solution:
    def swapNibbles (self, n):
        # Code here
        binaryN = bin(n)[2:]
        if len(binaryN) < 8:
            binaryN = "".join(['0' for _ in range(8 - len(binaryN))]) + binaryN
        return int(binaryN[4:] + binaryN[0:4], 2)
