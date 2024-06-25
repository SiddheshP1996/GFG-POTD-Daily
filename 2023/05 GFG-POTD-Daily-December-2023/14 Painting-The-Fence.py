# User function Template for python3

class Solution:
    def countWays(self, n, k):
        # Code here.
        mod = ((10 ** 9) + 7)
        if n == 1:
            return k

        previousNode, currentNode = 0, k
        result = previousNode + currentNode

        for i in range(2, n + 1):
            previousNode, currentNode = currentNode, (result * (k - 1)) % mod
            result = previousNode + currentNode

        return result % mod
