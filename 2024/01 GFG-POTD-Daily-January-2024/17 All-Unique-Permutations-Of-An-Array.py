# User function Template for python3

from itertools import permutations

class Solution:
    def uniquePerms(self, arr, n):
        # Code here
        unique_perms = set(permutations(arr))
        result = [list(perm) for perm in unique_perms]
        result.sort()
        return result