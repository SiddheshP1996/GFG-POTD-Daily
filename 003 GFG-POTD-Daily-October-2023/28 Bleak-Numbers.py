# User function Template for python3

import math


class Solution:
    def is_bleak(self, n):
        # Code here
        def count_bits(x):
            return int(math.floor(math.log2(x)))

        max_increase = count_bits(10 ** 9)

        for i in range(n, max(n - max_increase - 1, 0), -1):
            if i + bin(i)[2::].count("1") == n:
                return 0
        return 1
