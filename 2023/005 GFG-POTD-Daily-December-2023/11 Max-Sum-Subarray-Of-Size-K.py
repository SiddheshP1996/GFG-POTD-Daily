# User function Template for python3

class Solution:
    def maximumSumSubarray(self, K, Arr, N):
        # Code here
        # Initialize currentSummation and maxSummation with the sum of the first K elements
        currentSummation = maxSummation = sum(Arr[:K])

        # Slide the window
        for i in range(K, N):
            # Add the current element and subtract the first element of the previous window
            currentSummation = currentSummation + Arr[i] - Arr[i - K]

            # Update maxSummation
            maxSummation = max(maxSummation, currentSummation)

        return maxSummation
