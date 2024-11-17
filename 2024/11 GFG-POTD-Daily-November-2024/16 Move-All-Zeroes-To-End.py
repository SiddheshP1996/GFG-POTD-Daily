# User function Template for python3

class Solution:
    def pushZerosToEnd(self, arr):
        # Code here
        nonZeroIndex = 0

        for currentIndex in range(len(arr)):
            if arr[currentIndex] != 0:
                arr[nonZeroIndex], arr[currentIndex] = arr[currentIndex], arr[nonZeroIndex]
                nonZeroIndex += 1

        return arr
