# User function Template for python3
import heapq


class Solution:
    def maxCombinations(self, N, K, A, B):
        # Code here
        A = sorted(A, reverse=True)
        B = sorted(B, reverse=True)

        result = []
        l = []

        for i in range(N):
            heapq.heappush(l, (-(A[i] + B[0]), 0))

        while K:
            # print(l)
            curr = heapq.heappop(l)
            result.append(-curr[0])

            if curr[1] < N - 1:
                index = -(-curr[0] - B[curr[1]] + B[curr[1] + 1])
                heapq.heappush(l, (index, curr[1] + 1))
            K -= 1

        return result
