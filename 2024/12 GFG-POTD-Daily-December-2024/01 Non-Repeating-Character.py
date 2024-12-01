# User function Template for python3

from collections import Counter

class Solution:
    # Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self, s):
        # Code here
        a = Counter(s)
        for i, j in a.items():
            if j == 1:
                return i
                break
        return '$'
