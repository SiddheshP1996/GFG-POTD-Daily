# User function Template for python3

class Solution:
    def minimumStep(self, n, memoryVertex=None):
        # complete the function here
        if memoryVertex is None:
            memoryVertex = {}

        if n in memoryVertex:
            return memoryVertex[n]

        if n == 1:
            return 0

        if n % 3 == 0:
            results = 1 + self.minimumStep(n // 3, memoryVertex)
        else:
            results = 1 + self.minimumStep(n - 1, memoryVertex)

        memoryVertex[n] = results
        return results
