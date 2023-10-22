# User function Template for python3


class Solution:
    def find(self, arr, n, x):

        # code here
        indexList = []
        result = []

        if x not in arr:
            return [-1, -1]

        for i in range(len(arr)):
            if arr[i] == x:
                indexList.append(i)

        if len(indexList) == 1:
            result.append(indexList[0])
            result.append(indexList[0])
            return result
        else:
            result.append(indexList[0])
            result.append(indexList[-1])
            return result
