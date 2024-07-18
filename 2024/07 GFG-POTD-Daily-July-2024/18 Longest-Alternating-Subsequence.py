# User function Template for python3

class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
        # Code here
        lengthDecrease, lengthIncrease = 1, 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                lengthIncrease = lengthDecrease + 1
            elif arr[i] < arr[i - 1]:
                lengthDecrease = lengthIncrease + 1
        return max(lengthIncrease, lengthDecrease)
