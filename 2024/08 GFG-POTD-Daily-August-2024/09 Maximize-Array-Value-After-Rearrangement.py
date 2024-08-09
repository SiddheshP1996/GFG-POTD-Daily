# User function Template for python3

class Solution:
    def Maximize(self, arr): 
        # Complete the function
        mod = ((10 ** 9) + 7)
        arr.sort()
        result = 0
        
        for i in range(len(arr)):
            result += arr[i] * i
        
        return result % (mod)
