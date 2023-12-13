# User function Template for python3


class Solution:

    def countStrings(self, n):

        # Code here
        mod = 10 ** 9 + 7

        ewz = [0] * (n + 1)
        ewo = [0] * (n + 1)

        ewz[1] = 1
        ewo[1] = 1

        for i in range(2, n + 1):
            ewz[i] = (ewz[i - 1] + ewo[i - 1]) % mod
            ewo[i] = ewz[i - 1] % mod

        return (ewz[n] + ewo[n]) % mod
