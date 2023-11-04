# User function Template for python3

class Solution:
    def transitionPoint(self, arr, n):
        # Code here
        leftSideIndex = 0
        rightSideIndex = n
        while leftSideIndex < rightSideIndex:
            midOneIndex = (leftSideIndex + rightSideIndex) // 2
            if arr[midOneIndex] >= 1:
                rightSideIndex = midOneIndex
            else:
                leftSideIndex = midOneIndex + 1
        return leftSideIndex if leftSideIndex < n else -1
