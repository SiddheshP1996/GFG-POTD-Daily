# User function Template for python3

import sys

sys.setrecursionlimit((10 ** 5) // 5)


class Solution:

    def help(self, n, patternContainsList):
        patternContainsList.append(n)
        if n > 0:
            self.help(n - 5, patternContainsList)
            patternContainsList.append(n)

    def pattern(self, N):
        # code here
        patternContainsList = []
        self.help(N, patternContainsList)
        return patternContainsList
