# User function Template for python3

class Solution:
    def find3Numbers(self, arr):
        # Code Here
        arrayLength = len(arr)
        for i in range(arrayLength):
            for j in range(i + 1, arrayLength):
                for k in range(j + 1, arrayLength):
                    if arr[i] < arr[j] and arr[j] < arr[k]:
                        return (arr[i], arr[j], arr[k])
        return []
