# User function Template for python3

class Solution:
    def numberOfConsecutiveOnes (ob, n):
        # Code here
        fibonacci = [0,1]
        mod = ((10 ** 9) + 7)
        for i in range(2,n):
            fibonacci.append((fibonacci[i - 1] + fibonacci[i - 2]) % mod)

        result = [0, 1]
        for i in range(2, n):
            result.append((result[-1] * 2 + fibonacci[i]) % mod)

        return result[-1]
