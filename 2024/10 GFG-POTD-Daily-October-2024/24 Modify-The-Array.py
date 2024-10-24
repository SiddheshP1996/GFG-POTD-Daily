# User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        # Complete the function
        for i in range(len(arr) - 1):
            current = arr[i]
            if current == arr[i + 1]:
                arr[i] = 2 * arr[i]
                arr[i + 1] = 0
                
        arrOne = []
        
        for i in range(len(arr)):
            if arr[i] != 0:
                arrOne.append(arr[i])
        
        for i in range(len(arr) - len(arrOne)):
            arrOne.append(0)
            
        return arrOne
