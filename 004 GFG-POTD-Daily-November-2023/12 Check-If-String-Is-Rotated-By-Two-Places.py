# User function Template for python3


class Solution:
    # Function to check if a string can be obtained by rotating
    # another string by exactly 2 places.
    def isRotated(self, str1, str2):
        # code here
        if len(str1) < 2:
            return False
        return str1[2:] + str1[:2] == str2 or str1[-2:] + str1[:len(str1) - 2] == str2
