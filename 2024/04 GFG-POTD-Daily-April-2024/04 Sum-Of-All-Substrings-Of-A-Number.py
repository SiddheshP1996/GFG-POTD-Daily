# User function Template for python3

class Solution:
    # Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self, s):
        # Code here
        mod = ((10 ** 9) + 7)
        n = len(s)
        lastPointer = 0
        absentBox = 0
        for i in range(n):
            value = int(s[i])
            absentBox = ((absentBox * 10) + value * (i + 1)) % mod
            lastPointer = (lastPointer + absentBox) % mod
        return lastPointer
