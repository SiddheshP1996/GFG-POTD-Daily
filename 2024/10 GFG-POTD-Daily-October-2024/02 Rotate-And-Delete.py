# User function Template for python3

from typing import List
from collections import deque

class Solution:
    def rotateDelete(self, arr):
        # Code here
        arr = deque(arr)
        n = len(arr)
        
        for k in range(1, (n // 2) + 1):
            arr.appendleft(arr.pop())
            index = len(arr) - k
            del arr[index]
            
        return arr[0]
