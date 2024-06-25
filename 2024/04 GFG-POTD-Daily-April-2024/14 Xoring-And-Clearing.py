# User function Template for python3

class Solution:
    def printArr(self, n, arr):
        # Printing array elements with spaces
        for i in range(n):
            print(arr[i], end=" ")
        print()
        

    def setToZero(self, n, arr):
        # Setting all elements to zero
        for i in range(n):
            arr[i] = 0
        

    def xor1ToN(self, n, arr):
        # Doing xor with indices
        for i in range(n):
            arr[i] ^= i
