# User function Template for python3

from bisect import bisect_right

class Solution:
    def countElements(self, a, b, n, query, q):
        # Code here
        result = []
        elementsDictionary = {}
        b.sort()
        for i in range(n):
            index = bisect_right(b, a[i])
            if index >= n:
                elementsDictionary[i] = n
            else:
                elementsDictionary[i] = index
        for i in query:
            result.append(elementsDictionary[i])
        return result
