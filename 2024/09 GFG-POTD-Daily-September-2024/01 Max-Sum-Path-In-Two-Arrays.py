# Your task is to complete this function
# Function should return an integer denoting the required answer

class Solution:
    def maxPathSum(self, arr1, arr2):
        # Code here
        pointerOne, pointerTwo = 0, 0
        arr1Length, arr2Length = len(arr1), len(arr2)
        sum1, sum2 = 0, 0
        maxSum = 0
        
        while pointerOne < arr1Length and pointerTwo < arr2Length:
            if arr1[pointerOne] < arr2[pointerTwo]:
                sum1 += arr1[pointerOne]
                pointerOne += 1
            elif arr1[pointerOne] > arr2[pointerTwo]:
                sum2 += arr2[pointerTwo]
                pointerTwo += 1
            else:
                maxSum += max(sum1, sum2) + arr1[pointerOne]
                sum1, sum2 = 0, 0
                pointerOne += 1
                pointerTwo += 1
        
        while pointerOne < arr1Length:
            sum1 += arr1[pointerOne]
            pointerOne += 1
        
        while pointerTwo < arr2Length:
            sum2 += arr2[pointerTwo]
            pointerTwo += 1
        
        maxSum += max(sum1, sum2)
        
        return maxSum
