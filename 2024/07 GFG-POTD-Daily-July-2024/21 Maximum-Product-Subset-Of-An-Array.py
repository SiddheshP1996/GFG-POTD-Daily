# User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        # Write your code here
        mod = ((10 ** 9) + 7)
        minimum = float('inf')
        negative = False
        ret = 1
        for i in arr:
            if i == 0:
                continue
            if i < 0:
                i =- i
                minimum = min(minimum, i)
                negative = not negative
            ret = (ret * i) % mod
        if negative:
            ret = (ret // minimum) % mod
        return ret
