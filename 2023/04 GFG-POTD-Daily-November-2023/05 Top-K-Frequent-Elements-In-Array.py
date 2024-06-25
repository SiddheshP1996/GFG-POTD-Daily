# User function Template for python3

import collections
import heapq


class Solution:
    def topK(self, nums, k):
        # Code here
        noOfCounts = collections.defaultdict(int)
        for x in nums:
            noOfCounts[x] += 1
        noOfCountsNums = []
        for x, f in noOfCounts.items():
            noOfCountsNums.append((-f, -x))

        heapq.heapify(noOfCountsNums)

        results = []
        for i in range(k):
            results.append(-heapq.heappop(noOfCountsNums)[1])

        return results
