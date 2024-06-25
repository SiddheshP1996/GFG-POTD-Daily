# User function Template for python3

class Solution:
    def singleElement(self, arr, N):
        # Code here
        k = {}
        for i in arr:
            k[i] = k.get(i, 0) + 1
        
        for l, v in k.items():
            if v == 1:
                return l
        return -1
