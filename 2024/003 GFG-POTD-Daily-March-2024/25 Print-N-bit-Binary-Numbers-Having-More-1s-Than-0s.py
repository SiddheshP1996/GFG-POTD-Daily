# User function Template for python3

class Solution:
    def NBitBinary(self, n):
        # Code here
        result = []
        
        def oneOrZero(string, length, zeroes):
            if length == n:
                result.append(string)
                return
            
            oneOrZero(string + '1', length + 1, zeroes)
            
            if (length - zeroes) > zeroes:
                oneOrZero(string + '0', length + 1, zeroes + 1)
            
        oneOrZero('1', 1, 0)
        return result
