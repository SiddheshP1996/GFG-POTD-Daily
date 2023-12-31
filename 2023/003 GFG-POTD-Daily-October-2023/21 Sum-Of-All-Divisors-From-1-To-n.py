# User function Template for python3


class Solution:
    def sumOfDivisors(self, N):
        # code here
        result = 0
        for i in range(1, N + 1):
            k = N // i
            result = result + k * i
        return result
