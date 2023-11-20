# User function Template for python3

"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

from collections import defaultdict


class Solution:
    def sumK(self, root, k):
        # code here

        mod = ((10 ** 9) + 7)

        results = 0

        def pathRoute(nextPoint, cache, path=0):
            nonlocal results, k
            if not nextPoint:
                return

            current = path + nextPoint.data
            results += cache[current - k]
            cache[current] += 1

            pathRoute(nextPoint.left, cache, current)
            pathRoute(nextPoint.right, cache, current)
            cache[current] -= 1

        cache = defaultdict(int)
        cache[0] = 1
        pathRoute(root, cache)
        return results % mod
