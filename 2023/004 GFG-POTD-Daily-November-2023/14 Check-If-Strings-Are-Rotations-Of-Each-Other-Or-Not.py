# User function Template for python3

class Solution:

    # Function to check if two strings are rotations of each other or not.
    def areRotations(self, s1, s2):
        # code here
        # Check if the length of s1 and s2 are equal
        if len(s1) != len(s2):
            return False
        else:
            # Concatenate s1 with itself
            s1 = s1 + s1
            # Check if s2 is a substring of the concatenated string
            if s2 in s1:
                return True
            else:
                return False
            