# User function Template for python3

from collections import defaultdict

class Solution:
    def kTop(self,a, N, K):
        # Code here.
        result = []
        count = defaultdict(int)
        listOfNumbers = []
        for i, v in enumerate(a):
            count[v] += 1
            if count[v] == 1:
                listOfNumbers.append(v)
            listOfNumbers.sort(key = lambda x:(-count[x], x))
            result.append(listOfNumbers[:min(K, i + 1)])
        return result
