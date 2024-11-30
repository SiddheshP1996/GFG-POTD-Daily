# User function Template for python3

class Solution:
    
    # Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        # Code here
        return sorted(s1) == sorted(s2)
