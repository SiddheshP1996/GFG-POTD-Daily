# User function Template for python3

class Solution:
    def sumBitDifferences(self, arr, n):
        # Code here
        result = 0
        for i in range(32):
            count = 0
            for val in arr:
                if (val & (1 << i) != 0):
                    count += 1
            result += (count * (n - count) * 2)
        return result
