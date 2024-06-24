# User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # Code here
        if 2 <= q <= n + 1:
            return q - 1
        elif n + 1 < q <= 2 * n:
            return 2 * n - q + 1
        return 0
