# User function Template for python3

class Solution:
    def findNth(self, n):
        # Code here
        result, unitPlace = 0, 1
        while n:
            result += unitPlace * (n % 9)
            n //= 9
            unitPlace *= 10
        return result
