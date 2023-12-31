#User function Template for python3
import nums

class Solution:
    def singleNumber(self, nums):
        # Code here
        x=0
        for i in nums:
            x^=i

        t=1

        while not t&x:
            t <<= 1
        f=0;s=0

        for i in nums:
                if i&t:
                    s^=i
                else:
                    f^=i
        return sorted((f,s))