# User function Template for python3


class Solution:
    def minDist(self, arr, n, x, y):
        # code here
        lastSeenX = -1
        lastSeenY = -1
        results = 2 * n
        for i in range(n):
            if arr[i] == x:
                lastSeenX = i
            if arr[i] == y:
                lastSeenY = i
            if lastSeenY != -1 and lastSeenX != -1:
                results = min(results, abs(lastSeenY - lastSeenX))
        if results > n:
            return -1
        return results
