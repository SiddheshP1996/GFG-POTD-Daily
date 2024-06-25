# User function Template for python3

class Solution:
    def sequence(self, n):
        # Code here
        mod = ((10 ** 9) + 7)
        summ = 0
        add = 1
        
        for i in range(n):
            product = 1
            for j in range(i + 1):
                product = (product * add) % mod
                add += 1
            summ = (summ + product) % mod
        return summ
