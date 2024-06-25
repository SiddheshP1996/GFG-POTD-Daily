# User function Template for python3

class Solution:
    def findExtra(self, n, a, b):
        # Add code here
        result = list(set(a) - set(b))[0]
        return a.index(result)
