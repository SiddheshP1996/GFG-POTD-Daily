# User function Template for python3

from collections import deque
from functools import reduce

class Solution:
    """
    Complete this function
    function to convert a given Gray equivalent n to Binary equivalent.
    """
    def grayToBinary(self, n):
        # Your code here
        q = deque()
        while n > 0:
            q.appendleft(n % 2)
            n //= 2
        
        retrievedBits = []
        for b in q:
            if not retrievedBits:
                retrievedBits.append(b)
            else:
                retrievedBits.append(retrievedBits[-1] ^ b)
        return reduce(lambda v, e: v*2+e, retrievedBits, 0)
