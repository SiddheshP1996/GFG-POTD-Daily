# User function Template for python3

from typing import List


class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        # Code here
        arr.sort()
        
        integerSet = set()
        for i in reversed(arr):
            if x + i in integerSet:
                return 1
            integerSet.add(i)
            
        return -1
