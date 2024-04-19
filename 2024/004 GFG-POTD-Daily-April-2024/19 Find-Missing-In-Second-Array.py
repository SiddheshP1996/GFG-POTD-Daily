# User function Template for python3

from collections import defaultdict

class Solution:
    def findMissing(self, a, b, n, m):
        # Code here
        result = []
        dKaDict = defaultdict(int)
        for i in b:
            dKaDict[i] = 1
            
        for i in a:
            if dKaDict[i] == 0:
                result.append(i)
        return result