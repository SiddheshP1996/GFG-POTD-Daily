# User function Template for python3

class Solution:
    def lps(self, str):
        # Code here
        stringLength = len(str)
        lpsArray = [0] * stringLength

        index = 1
        length = 0

        while index < stringLength:
            if str[index] == str[length]: 
                length += 1
                lpsArray[index] = length
                index += 1
            else:
                if length != 0: length = lpsArray[length - 1]
                else: index += 1

        return lpsArray[-1]
