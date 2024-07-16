# User function Template for python3

class Solution:
    def printString(self, s, ch, count):
        # Code here
        for i, char in enumerate(s):
            if char == ch:
                count -= 1
            if count == 0:
                return s[i + 1:]
        return ""
