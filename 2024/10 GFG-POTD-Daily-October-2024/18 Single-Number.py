# User function Template for python3

class Solution:    
    def getSingle(self, arr):
        # Code here
        arrDict = {}
        
        for i in arr:
            arrDict[i] = arrDict.get(i, 0) + 1
        
        for i in arrDict:
            if arrDict[i] & 1:
                return i
