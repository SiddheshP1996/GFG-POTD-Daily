from collections import deque


class Solution:
    # Back-end complete function Template for Python 3
    # Function to find the leaders in the array.
    def leaders(self, A, N):
        # Code here
        res = deque([A[N - 1]])
        for i in range(N - 2, -1, -1):
            if res[0] <= A[i]:
                res.appendleft(A[i])
        return res
