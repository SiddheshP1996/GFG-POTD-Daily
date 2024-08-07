# User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        # Code here
        arr1 = sorted(arr1 + arr2)
        return arr1[k - 1]
