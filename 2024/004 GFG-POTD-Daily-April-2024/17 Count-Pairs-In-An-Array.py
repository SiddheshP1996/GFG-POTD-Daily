# User function Template for python3

from bisect import bisect_left, insort

class Solution:    
    def countPairs(self, arr, n): 
        # Your code goes here
        newArray = [i * j for i, j in enumerate(arr)]
        result = 0
        lis = []
        
        for i in range(n - 1, -1, -1):
            if not lis:
                insort(lis, newArray[i])
                continue
            result += bisect_left(lis, newArray[i])
            insort(lis, newArray[i])
        return result
