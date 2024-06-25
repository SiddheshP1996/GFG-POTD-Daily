# User function Template for python3

class Solution:
    def game_with_number (self, arr,  n) : 
        # Complete the function
        for item in range(n - 1):
            arr[item] |= arr[item + 1]
        return arr
