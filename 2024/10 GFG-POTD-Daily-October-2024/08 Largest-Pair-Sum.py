# User function Template for python3

from typing import List

class Solution:
    def pairsum(self, arr : List[int]) -> int:
        # Code here
        num1, num2 = 0, 0
        for i in range(len(arr)):
            if arr[i] >= num1:
                num2 = num1
                num1 = arr[i]
            elif arr[i] >= num2 and arr[i] < num1:
                num2 = arr[i]
        return num1 + num2
