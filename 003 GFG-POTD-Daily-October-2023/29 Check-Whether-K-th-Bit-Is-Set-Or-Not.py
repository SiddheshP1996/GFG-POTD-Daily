# User function Template for python3


class Solution:

    # Function to check if Kth bit is set or not.
    def checkKthBit(self, n, k):
        # Your code here
        return n & (1 << k) == (1 << k)
