# User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # Code here
        result = sorted(arr1 + arr2)
        n = len(result) // 2
        return result[n - 1] + result[n]
