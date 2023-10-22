# User function Template for python3

class Solution:
    def substrCount(self, s, k):
        # your code here
        last, totalSubstrings = [-1] * 26, []
        result = 0
        for i, c in enumerate(s):
            value = ord(c) - 97
            if last[value] >= 0:
                totalSubstrings.remove(last[value])
            last[value] = i
            totalSubstrings.append(i)
            M = len(totalSubstrings)
            if M > k:
                result += totalSubstrings[-k] - totalSubstrings[-k - 1]
            elif M == k:
                result += totalSubstrings[0] + 1
        return result
