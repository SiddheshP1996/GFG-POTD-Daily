# User function Template for python3

class Solution:
    def nthPoint(self, n):
        # Code here
        mod = ((10 ** 9) + 7)
        wayToPoint = [0] * (n + 1)

        wayToPoint[0] = 1
        wayToPoint[1] = 1

        for i in range(2, n + 1):
            wayToPoint[i] = (wayToPoint[i - 1] + wayToPoint[i - 2]) % mod

        return wayToPoint[n]
