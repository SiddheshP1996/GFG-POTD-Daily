# User function Template for python3

class Solution:

    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self, arr, n):
        # Your code here
        # Return true or false
        counter = 0
        map = {0: 1}
        localSumInSubarray = 0

        for i in range(len(arr)):
            localSumInSubarray += arr[i]

            if localSumInSubarray in map:
                counter += map[localSumInSubarray]

            map[localSumInSubarray] = map.get(localSumInSubarray, 0) + 1

        return counter
