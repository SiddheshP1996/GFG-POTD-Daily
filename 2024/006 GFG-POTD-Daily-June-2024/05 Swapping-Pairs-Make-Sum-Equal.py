# User function Template for python3

class Solution:
    def findSwapValues(self, a, n, b, m):
        # Your code goes here
        setOfA = set(a)
        setOfB = set(b)
        sumOfA = sum(a)
        sumOfB = sum(b)
        if sumOfA == sumOfB:
            return 1
        difference = abs(sumOfA - sumOfB)
        if difference & 1 == 1:
            return -1
        for x in setOfA:
            if difference - x in setOfB:
                return 1
        return -1