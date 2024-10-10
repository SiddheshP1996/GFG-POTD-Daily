# User function Template for python3

class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        indexMap = {}
        maxDist = 0
        for index, value in enumerate(arr):
            if value in indexMap:
                distance = index - indexMap[value]
                maxDist = max(maxDist, distance)
            else:
                indexMap[value] = index
        return maxDist
