# User function Template for python3

class Solution:
    def countgroup(self, arr): 
        result = 0
        for i in arr:
            result ^= i

        if result == 0:
            return pow(2, len(arr) - 1) - 1

        return 0
