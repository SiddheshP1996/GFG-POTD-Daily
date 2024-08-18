# User function Template for python3

class Solution:
    def canSplit(self, arr):
        # Code here
        arrLength = len(arr)
        leftSum = arr[0]
        rightSum = arr[arrLength - 1]
        
        pointerOne = 0
        pointerTwo = arrLength - 1
        
        while pointerOne < pointerTwo:
            if (leftSum == rightSum and pointerOne + 1 == pointerTwo):
                return True
            elif (leftSum > rightSum):
                pointerTwo -= 1
                rightSum += arr[pointerTwo]
            else:
                pointerOne += 1
                leftSum += arr[pointerOne]
        return False
