# User function Template for python3

class Solution:
    
    # Function to find maximum of each subarray of size k.
    def max_of_subarrays(self, k, arr):
        # Code here
        result = []
        currentMax = max(arr[:k])
        result.append(currentMax)
        
        for i in range(1, len(arr) - k + 1):
            if arr[i - 1] == currentMax:
                currentMax = max(arr[i:i + k])
            else:
                currentMax = max(currentMax, arr[i + k - 1])
            result.append(currentMax)
        return result
