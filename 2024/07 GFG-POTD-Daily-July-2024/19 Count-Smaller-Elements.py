# User function Template for python3

from sortedcontainers import SortedList

class Solution:

    def constructLowerArray(self, arr):
        # Code here
        sortList = SortedList()
        result = [0 for i in range(len(arr))]

        for i in reversed(range(len(arr))):
            sortList.add(arr[i])
            result[i] = sortList.index(arr[i])

        return result
