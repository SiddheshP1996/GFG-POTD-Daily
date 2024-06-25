# User function Template for python3

class Solution:
    def pushZerosToEnd(self, arr, n):
        # code here
        totalNumberOfZeros = arr.count(0)

        toBeReplace = -1
        realZeroesPosition = 0
        for i in range(n):
            if arr[i] != 0:
                arr[realZeroesPosition] = arr[i]
                realZeroesPosition += 1
        for i in range(n - totalNumberOfZeros, n):
            arr[i] = 0
        return arr
    