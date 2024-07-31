# User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # Code here
        if not arr:
            return "-1"
        prefix = arr[0]
        for string in arr[1:]:
            i = 0
            while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
                i += 1
            prefix = prefix[:i]
            if not prefix:
                return "-1"
        return prefix
