# User function Template for python3

from bisect import bisect_right
from math import log

class Solution:
    
     # Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(self, arr, brr):
        # Code here
        """
            x^y > y^x
            y logx > x logy
            y / logy > x / logx
            logy / y < logx/x
        """
        arrLength = len(arr)
        brrLength = len(brr)
        a = [] * arrLength
        b = [] * brrLength
        count = 0
        for y in arr:
            a.append(log(y) / y)
            
        for x in brr:
            b.append(log(x) / x)
        
        a.sort()
        b.sort()
        
        for i in range(brrLength):
            index = bisect_right(a, b[i])
            count += arrLength - index
        
        return count
