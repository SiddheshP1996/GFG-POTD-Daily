# User function Template for python3

class Solution:
    def isLucky(self, n):
        # RETURN True OR False
        count = 2
        while count <= n:
            if n % count == 0:
                return False
            n = n - (n // count)
            count += 1
        return True
