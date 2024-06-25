# User function Template for python3

from typing import List
from collections import defaultdict

class Solution:
    def longestSubseq(self, n : int, a : List[int]) -> int:
        # Code here
        mapping = defaultdict(int)
        result = float("-inf")
        for item in range(n):
            mapping[a[item]] = max(mapping[a[item] - 1], mapping[a[item] + 1]) + 1
            result = max(result, mapping[a[item]])
        return result
