# User function Template for python3

class Solution:
    def gameOfXor(self, N , A):
        # Code here
        # initializing the result as 0
        result = 0
        # iterating over all array elements
        for i in range(len(A)):
            # calculate the frequency of A[i] in the entire subarrays
            frequencyToCalculate = (i + 1) * (len(A) - i)
            # if the frequency is odd, include A[i] in the result
            if frequencyToCalculate % 2 == 1:
                result ^= A[i]
        # returning final result
        return result
