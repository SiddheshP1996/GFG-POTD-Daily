# User function Template for python3

class Solution:
    mod = ((10 ** 9) + 7)
    
    def series(self, n):
        # Code here
        result = [0, 1]
        
        for i in range(n - 1):
            result.append((result[-1] + result [-2]) % self.mod)
        return result if n else [0]
