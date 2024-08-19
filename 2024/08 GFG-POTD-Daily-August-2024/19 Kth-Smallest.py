# User function Template for python3

class Solution:

    def kthSmallest(self, arr, k):
        arr = sorted(arr)
        return arr[k - 1]
