# User function Template for python3

class Solution:
    def kPangram(self, string, k):
        # Code here
        totalCharacters, uniqueCharacters, isPresent = 0, 0, [False] * 26
        
        for value in string:
            if value.isalpha():
                totalCharacters += 1
                i = ord(value) - ord("a")
                
                if not isPresent[i]:
                    isPresent[i] = True
                    uniqueCharacters += 1
                    
        return 26 - uniqueCharacters <= k and totalCharacters >= 26
