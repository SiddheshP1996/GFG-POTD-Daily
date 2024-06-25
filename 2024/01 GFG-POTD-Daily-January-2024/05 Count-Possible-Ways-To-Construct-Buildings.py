# User function Template for python3

class Solution:
    def TotalWays(self, N):
        # Code here
        numA, numB = 1, 1
        mod = ((10 ** 9) + 7)
        for i in range(1, N + 1):
            numA, numB = numB % mod, (numA % mod + numB % mod) % mod
        return (numB ** 2) % mod
