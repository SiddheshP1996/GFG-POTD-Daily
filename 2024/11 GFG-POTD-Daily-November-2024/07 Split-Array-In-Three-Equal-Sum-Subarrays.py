# User function Template for python3
class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        totalSum = sum(arr)
        if totalSum % 3 != 0:
            return [-1, -1]
        partSum = totalSum // 3
        currentSum = 0
        i, j = -1, -1
        
        for index in range(len(arr)):
            currentSum += arr[index]
            if currentSum == partSum:
                i = index
                break
            
        if i == -1:
            return [-1, -1]
        currentSum = 0
        for index in range(i + 1, len(arr)):
            currentSum += arr[index]
            if currentSum == partSum:
                j = index
                break
            
        if j == -1 or j == len(arr) - 1:
            return [-1, -1]
        return [i, j]
