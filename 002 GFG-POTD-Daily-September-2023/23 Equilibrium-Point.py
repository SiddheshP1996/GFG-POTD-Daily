# User function Template for python3

class Solution:
    # Complete this function

    # Function to find equilibrium point in the array.
    def equilibriumPoint(self, A, N):
        # Your code here
        if N == 1:
            return 1
        else:
            leftSum, rightSum = 0, sum(A)
            for i in range(0, N):
                rightSum -= A[i]
                if leftSum == rightSum:
                    return i + 1
                leftSum += A[i]
            return -1
