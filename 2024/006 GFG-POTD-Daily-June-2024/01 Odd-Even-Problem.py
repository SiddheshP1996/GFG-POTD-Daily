# User function Template for python3

class Solution:
    def oddEven(self, s : str) -> str:
        # Code here
        lettersFrequency = {}
        for letter in s:
            lettersFrequency[letter] = lettersFrequency.get(letter, 0) + 1
        
        result = 0
        for key in lettersFrequency:
            if ord(key) % 2 == lettersFrequency[key] % 2:
                result += 1
        
        if result % 2 == 0:
            return "EVEN"
        return "ODD"
