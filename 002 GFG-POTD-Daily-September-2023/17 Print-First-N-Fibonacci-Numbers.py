# User function Template for python3

class Solution:
    # Function to return list containing first n fibonacci numbers.
    def printFibb(self, n):
        # your code here
        res = [1, 1]
        for i in range(3, n + 1):
            res.append(res[-1] + res[-2])
        return res if n > 1 else [1]
