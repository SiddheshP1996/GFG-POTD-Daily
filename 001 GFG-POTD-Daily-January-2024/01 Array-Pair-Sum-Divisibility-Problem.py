# User function Template for python3

class Solution:
    def canPair(self, nuns, k):
        # Code here
        nunStorage = {}
        for n in nuns:
            nunStorage[n % k] = nunStorage.get(n % k, 0) + 1
            x = (k - n % k) % k
            if x in nunStorage and nunStorage[x] != 0:
                nunStorage[x] -= 1
                nunStorage[n % k] -= 1

        for i in nunStorage:
            if nunStorage[i] != 0:
                return False

        return True
