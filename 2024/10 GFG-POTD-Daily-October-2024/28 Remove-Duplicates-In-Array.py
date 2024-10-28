# User function Template for python3

class Solution:
    def removeDuplicates(self, arr):
        # Code here
        resultList = []
        for element in arr:
            if element not in resultList:
                resultList.append(element)
        return resultList
