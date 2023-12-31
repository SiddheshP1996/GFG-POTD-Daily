# User function Template for python3

class Solution:
    def isPerfectNumber(self, N):
        # code here
        if N <= 1:
            return 0

        # Initialize the sum of factors to 1 (1 is always a factor)
        factor_sum = 1

        # Iterate from 2 to the square root of N
        for i in range(2, int(N ** 0.5) + 1):
            if N % i == 0:
                # Add both the divisor and its corresponding factor to the sum
                factor_sum += i
                if i != N // i:
                    factor_sum += N // i

        # Check if the sum of factors is equal to N
        if factor_sum == N:
            return 1
        else:
            return 0