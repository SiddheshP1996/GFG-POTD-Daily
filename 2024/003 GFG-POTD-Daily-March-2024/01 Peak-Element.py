# User function template for Python

# Your task is to complete this function
# Function should return index to the any valid peak element

class Solution:   
    def peakElement(self, arr, n):
        # Code here
        if n == 1 or arr[0] >= arr[1]:
            return 0
            
        if arr[n - 1] >= arr[n - 2]:
            return n - 1
        
        for element in range(1, n - 1):
            if arr[element - 1] <= arr[element] >= arr[element + 1]:
                return element
                
        return -1
