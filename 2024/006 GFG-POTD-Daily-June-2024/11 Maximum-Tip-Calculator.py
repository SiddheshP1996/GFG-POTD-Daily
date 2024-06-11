# User function Template for python3

from typing import List

class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        # Code here
        orders = [(arr[i], brr[i], arr[i] - brr[i]) for i in range(n)]
        orders.sort(key = lambda x: abs(x[2]), reverse = True)
        
        totalTip = 0
        collectionOfA, collectionOfB = 0, 0
        
        for tipOfA, tipOfB, tipDifference in orders:
            
            if (tipDifference >= 0 and collectionOfA < x) or collectionOfB >= y:
                totalTip += tipOfA
                collectionOfA += 1
            else:
                totalTip += tipOfB
                collectionOfB += 1
                
        return totalTip
