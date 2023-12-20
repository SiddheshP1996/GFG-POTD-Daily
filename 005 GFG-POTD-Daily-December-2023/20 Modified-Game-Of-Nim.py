# User function Template for python3

class Solution:
    def findWinner(self, n, A):
        # Code here
        result = 0
        for i in range(n):
            result ^= A[i]
        
        return 1 if not result else (n % 2) + 1
