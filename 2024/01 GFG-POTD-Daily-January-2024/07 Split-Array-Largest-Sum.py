# User function Template for python3

class Solution:
    def binarySearch(self, arr, divSum):
        numberOfDiv, currentSum = 1, 0
        for a in arr:
            if currentSum + a <= divSum:
                currentSum += a
            else:
                numberOfDiv += 1
                currentSum = a
        return numberOfDiv

    def splitArray(self, arr, N, K):
        # Code here
        leftItem, rightItem = max(arr), sum(arr)
        while leftItem <= rightItem:
            midddleItem = (leftItem + rightItem) // 2
            currrrentItem = self.binarySearch(arr, midddleItem)
            if currrrentItem > K:
                leftItem = midddleItem + 1
            else:
                rightItem = midddleItem - 1
        return leftItem
