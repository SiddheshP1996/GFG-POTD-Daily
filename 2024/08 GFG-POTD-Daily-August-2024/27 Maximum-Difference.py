# User function Template for python3

class Solution:
    def findMaxDiff(self, arr):
        # Code here
        n = len(arr)
        left, right = [0] * n, [0] * n
        
        arrStack = []
        for i in range(n):
            while(arrStack and arr[arrStack[-1]] >= arr[i]):
                arrStack.pop()
                
            if arrStack:
                left[i] = arr[arrStack[-1]]
            arrStack.append(i)
        arrStack = []
        
        for i in range(n - 1, -1, -1):
            while(arrStack and arr[arrStack[-1]] >= arr[i]):
                arrStack.pop()
                
            if arrStack:
                right[i] = arr[arrStack[-1]]
            arrStack.append(i)
        result = -1e9
        
        for i in range(n):
            result = max(result, abs(left[i] - right[i]))
        return result
