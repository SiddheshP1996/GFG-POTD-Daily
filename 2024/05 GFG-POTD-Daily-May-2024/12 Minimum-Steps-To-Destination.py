# User function Template for python3

class Solution:
    def minSteps(self, d):
        # Code here
        for i in range(1, (2 * d)):
            if (((i * (i + 1)) // 2) + d) % 2 == 0 and ((i * (i + 1)) // 2) >= d:
                return i
