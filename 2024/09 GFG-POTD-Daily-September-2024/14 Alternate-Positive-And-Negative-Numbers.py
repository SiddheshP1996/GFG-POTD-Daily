# User function Template for python3

from itertools import zip_longest

class Solution:
    def rearrange(self, arr):
        positive = [item for item in arr if item >= 0]
        negative = [item for item in arr if item < 0]
        
        arr[:] = [x for pair in zip_longest(positive, negative)\
            for x in pair if x is not None]
