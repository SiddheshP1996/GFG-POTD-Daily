# User function Template for python3

class Solution:
    def findTriplet(self, arr):
        # Code here
        visited = set(arr)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] in visited:
                    return True
        return False
