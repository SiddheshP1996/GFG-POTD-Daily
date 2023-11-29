# User function Template for python3

class Solution:
    def isEulerCircuitExist(self, V, adj):
        # Code here
        odd = 0
        for item in adj:
            if len(item) % 2 == 1:
                odd += 1
        if odd == 0:
            return 2
        elif odd == 2:
            return 1
        return 0
