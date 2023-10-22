# User function Template for python3


class Solution:
    def isPalindrome(self, S):
        # code here
        count = 0
        if S == S[::-1]:
            return count + 1
        else:
            return 0
