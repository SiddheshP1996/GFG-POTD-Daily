# User function Template for python3

from typing import List


class Solution:
    def convertToWave(self, n: int, a: List[int]) -> None:
        # code here
        # Iterate through the array in steps of 2 and swap adjacent elements
        for i in range(0, n - 1, 2):
            a[i], a[i + 1] = a[i + 1], a[i]
