# User function Template for python3

import sys


class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        cache = {}
        sys.setrecursionlimit(10 ** 8)

        def go(W):
            if W in cache:
                return cache[W]
            best = 0
            for i in range(N):
                if wt[i] <= W:
                    best = max(best, val[i] + go(W - wt[i]))
            cache[W] = best
            return best

        return go(W)
