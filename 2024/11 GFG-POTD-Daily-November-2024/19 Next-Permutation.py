# User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        # Code here
        n = len(arr)
        i = n - 2

        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        if i >= 0:
            for j in range(n - 1, i, -1):
                if arr[j] > arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
                    break

        left, right = i + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
