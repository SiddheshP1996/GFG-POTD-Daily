# User function Template for python3
from functools import cmp_to_key

class Solution:

    def printLargest(self, n, arr):
        # Code here
        def compare(x, y):
            xy = x + y
            yx = y + x
            
            if xy > yx:
                return -1
            elif yx > xy:
                return 1
            else:
                return 0
    
        arr.sort(key = cmp_to_key(compare))
        
        largestDigit = "".join(arr)
        
        return largestDigit
