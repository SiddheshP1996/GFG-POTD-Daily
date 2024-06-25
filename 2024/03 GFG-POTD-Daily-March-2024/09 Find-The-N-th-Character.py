# User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        # Code here
        corelation = {
            '1': '10',
            '0': '01'
        }
        
        r = 1 << r
        
        while r > 1:
            characterIndex = n // r
            s = corelation[s[characterIndex]]
            if n >= r:
                n %= r
            r //= 2
            
        return s[n // r]
