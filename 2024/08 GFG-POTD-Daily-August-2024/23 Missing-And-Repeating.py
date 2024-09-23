# User function Template for python3

class Solution:
    def findTwoElement(self, arr): 
        # Code here
        arrLength = len(arr)
        arr.sort()
        duplicate = None
        totalSum = sum(arr)
        for i in range(1, arrLength):
            if arr[i] == arr[i - 1]:
                duplicate = arr[i]
                break
            
        sumation = arrLength * (arrLength + 1) // 2
        missingNumber = sumation - (totalSum - duplicate)
        return duplicate, missingNumber
