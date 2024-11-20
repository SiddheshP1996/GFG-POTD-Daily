# User function Template for python3

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        # Your Code goes here.
        arr.sort()
        n = len(arr) // 3
        count = 1
        result = []
        
        if len(arr)> 1 and arr[0] == arr[1]:
            count = 2
        else:
            count = 1
            
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                count += 1
            else:
                if count > n:
                    result.append(arr[i - 1])
                count = 1
                
        if count > n:
            result.append(arr[-1])
            
        return result
