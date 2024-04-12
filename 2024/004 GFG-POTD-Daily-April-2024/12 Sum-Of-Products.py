# User function Template for python3

class Solution:
    def pairAndSum(self, n, arr):
        # Code here
        result = 0
        for i in range(32):
            c = 0
            
            for j in arr:
                if (j >> i) & 1:
                    c += 1
            
            if c > 1:
                result += (2 ** i) * ((c - 1) * c) // 2
        
        return result
