# User function Template for python3

class Solution:
    def countPairsWithDiffK(self, arr, k):
        # Code here
        differenceDict = {}
        count = 0 
        for i in arr:
            if i + k not in differenceDict:
                differenceDict[i + k] = 1
            else:
                differenceDict[i + k] += 1

            if i - k not in differenceDict:
                differenceDict[i - k] = 1
            else:
                differenceDict[i - k] += 1

            if i in differenceDict:
                count += differenceDict[i]
        return count
