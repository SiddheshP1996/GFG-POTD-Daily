# User function Template for python3

class Solution:
    def DivisibleByEight(self, s):
        # Code here
        number = int(s[-3:])
        if number % 8 == 0:
            return 1
        return -1
