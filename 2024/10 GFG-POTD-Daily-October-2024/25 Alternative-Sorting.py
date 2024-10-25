# User function Template for python3

class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        result = []
        leftElement, rightElement = 0, len(arr) - 1
        
        while leftElement <= rightElement:
            if leftElement <= rightElement:
                result.append(arr[rightElement])
                rightElement -= 1
                
            if leftElement <= rightElement:
                result.append(arr[leftElement])
                leftElement += 1
        
        return result
