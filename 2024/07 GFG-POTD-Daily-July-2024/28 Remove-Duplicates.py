# User function Template for python3

class Solution:
    def removeDups(self, str):
        # Code here
        isPresent = [False] * 26
        result = ""
        for value in str:
            i = ord(value) - ord("a")
            if not isPresent[i]:
                result += value
                isPresent[i] = True
        return result
