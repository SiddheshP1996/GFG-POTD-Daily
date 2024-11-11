# User function Template for python3

class Solution:
    def minIncrements(self, arr): 
        # Code here
        arr.sort()
        result = 0
        length = len(arr)
        
        for i in range(1 , length):
            if arr[i] == arr[i - 1]:
                arr[i] += 1
                result += 1
            
            elif arr[i] < arr[i - 1]:
                result += (arr[i - 1] + 1) - arr[i]
                arr[i] = arr[i - 1] + 1
        
        return result
