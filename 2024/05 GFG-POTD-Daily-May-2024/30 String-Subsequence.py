# User function Template for python3

class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        # Code here
        n, m, mod = len(s1), len(s2), ((10 ** 9) + 7)
        
        previous = [0] * (m + 1)
        previous[m] = 1
        for i in range(n - 1, -1, -1):
            current = [0] * (m + 1)
            current[m] = 1
            for j in range(m - 1, -1, -1):
                result = previous[j] % mod
                if s1[i] == s2[j]:
                    result += previous[j + 1] % mod
                current[j] = result % mod
            previous = [k for k in current]
        return current[0] % mod
