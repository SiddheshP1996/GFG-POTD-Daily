# User function Template for python3

class Solution():
    def maxSumWithK(self, a, n, k):
        # Code here
        summation = 0
        for i in range(k):
            summation += a[i]
            
        keepTrackOfElementsSum = 0
        # Keep track of starting index of current sub-array
        j = 0

        result = float('-inf')
        result = max(result, summation)
        for i in range(k, n):
            summation += a[i]
            keepTrackOfElementsSum += a[j]
            
            j += 1
            result = max(result, summation)
            if (keepTrackOfElementsSum < 0):
                summation -= keepTrackOfElementsSum
                result = max(result, summation)
                keepTrackOfElementsSum = 0
                
        return result
