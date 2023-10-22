# User function Template for python3

class Solution:
    def numberOfPaths (self, M, N):
        # print(a)
        pass
        # code here
        pathToTravel = 1
        MOD = ((10 ** 9) + 7)
        for i in range(M - 1):
            pathToTravel = (pathToTravel * (i + N)) % MOD
            temp = pow(i + 1, MOD - 2, MOD)
            pathToTravel = (pathToTravel * temp ) % MOD
        return pathToTravel
