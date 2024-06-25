# User function Template for python3

from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # Code here
        lowNum, highNum = 0, n - 1
        while lowNum <= highNum:
            middleNum = (lowNum + highNum) // 2
            if k < arr[middleNum]:
                if middleNum == 0 or arr[middleNum] - k <= k - arr[middleNum - 1]:
                    return arr[middleNum]
                else:
                    highNum = middleNum - 1
            else:
                if middleNum == n - 1 or k - arr[middleNum] < arr[middleNum + 1] - k:
                    return arr[middleNum]
                else:
                    lowNum = middleNum + 1
