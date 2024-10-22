# User function Template for python3

from collections import Counter

class Solution:
    def sameOccurrence(self, arr, x, y):
        # Code here        
        count = Counter({0: 1})
        subArr, result = 0, 0
        for equalAmount in arr:
            if equalAmount == x:
                subArr += 1
            elif equalAmount == y:
                subArr -= 1
            result += count[subArr]
            count[subArr] += 1
        return result
