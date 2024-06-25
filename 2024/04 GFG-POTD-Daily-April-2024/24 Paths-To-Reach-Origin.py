# User function Template for python3

class Solution:
    def ways(self, n, m):
        # write you code here
        mod = ((10 ** 9) + 7)
        result = 1
        for i in range(1, m + 1):
            result = result * (m + n + 1 - i) // (i)
        return result % mod
