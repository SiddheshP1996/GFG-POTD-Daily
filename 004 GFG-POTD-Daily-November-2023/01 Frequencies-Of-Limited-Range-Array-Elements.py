# User function Template for python3

class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        def go(i):
            if i >= N:
                return
            if arr[i] <= 0:
                arr[i] -= 1
                return
            nextNumber = arr[i] - 1

            arr[i] = 0
            go(nextNumber)
            arr[i] -= 1

        for i in range(N):
            if arr[i] > 0:
                indexOfNumber = arr[i] - 1
                arr[i] = 0
                go(indexOfNumber)

        for i in range(N):
            arr[i] = abs(arr[i])
        return arr
