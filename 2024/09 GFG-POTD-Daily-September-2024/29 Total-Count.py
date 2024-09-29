# User function Template for python3

class Solution:
    def totalCount(self, k, arr):
        # Code here
        count = 0
        
        for i in range(len(arr)):
            divisor = arr[i] // k
            remainder = arr[i] % k
            
            if remainder != 0:
                divisor += 1
            
            count += divisor
        return count
