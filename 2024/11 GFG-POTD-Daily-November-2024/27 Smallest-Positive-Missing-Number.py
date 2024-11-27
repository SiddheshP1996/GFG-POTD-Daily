# User function Template for python3

class Solution:
    
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        # Your code here
        visit = set(arr)
        i = 1
        while(i in visit):
            i += 1
        return i
