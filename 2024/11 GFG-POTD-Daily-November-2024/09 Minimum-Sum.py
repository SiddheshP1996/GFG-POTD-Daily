# User function Template for python3

from collections import deque

class Solution:
    def minSum(self, arr):
        # Code here
        arr.sort(reverse = True)
        result = deque()
        carry = 0
        i = 0
        while i < len(arr) and arr[i] != 0:
            val = arr[i] + carry
            if (i + 1) < len(arr):
                val += arr[i + 1]
            carry = val // 10
            val = val % 10
            result.appendleft(str(val))
            i += 2
        if carry:
            result.appendleft("1")
        return "".join(result)
