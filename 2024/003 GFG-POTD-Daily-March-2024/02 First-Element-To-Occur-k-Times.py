# User function Template for python3

class Solution:
    def firstElementKTime(self, n, k, a):
        # Code here
        dictCount = {}
        for num in a:
            dictCount[num] = dictCount.get(num, 0) + 1
            if dictCount[num] == k:
                return num
        return -1
