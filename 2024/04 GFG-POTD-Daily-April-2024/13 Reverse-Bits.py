# User function Template for python3

class Solution:
    def reversedBits(self, x):
        # Code here
        y = bin(x)[2:]
        b = y.zfill(32)
        z = b[::-1]
        result = int(z, 2)
        return result
