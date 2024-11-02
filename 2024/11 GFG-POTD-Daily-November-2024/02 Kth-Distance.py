# User function Template for python3

class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # Your code
        duplicateSeen = {}
        for i in range(len(arr)):
            if arr[i] in duplicateSeen and i - duplicateSeen[arr[i]] <= k:
                return True
            duplicateSeen[arr[i]] = i
        return False
