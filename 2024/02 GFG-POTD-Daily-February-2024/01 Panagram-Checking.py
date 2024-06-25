# User function Template for python3

class Solution:
    
    # Function to check if a string is Pangram or not.
    def checkPangram(self, s):
        # Code here
        # Convert to lower case
        lower_string_s = s.lower()
        # All 26 letters of english
        letters = [chr(a) for a in range(97, 97 + 26)] 
        
        # all() returns True only if all elements inside an iterable is True
        return all([(letter in lower_string_s) for letter in letters])
