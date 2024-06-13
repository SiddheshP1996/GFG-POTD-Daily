# User function Template for python3

class Solution:
    def padovanSequence(self, n):
        # Code here
        mod = ((10 ** 9) + 7)
        if n == 0 or n == 1 or n == 2:
            return 1
        
        previousKaPrevious = 1
        previous = 1
        current = 1
        nextOne = 1
        
        for i in range(3, n + 1):
            nextOne=(previousKaPrevious + previous) % mod
            previousKaPrevious = previous
            previous = current
            current = nextOne
        return nextOne % mod
