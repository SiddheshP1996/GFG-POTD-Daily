# User function Template for python3

class Solution:
    def longestCommonSubstr(self, str1, str2):
        # Code here
        maximumLength=0
        for i in range(len(str1)):
            for j in range(i, len(str1)):
                string = str1[i:j + 1]
                if string in str2:
                    maximumLength = max(maximumLength, len(string))
        return maximumLength
