# User function Template for python3

class Solution:
    def printClosest(self, arr, brr, n, m, x):
        # code here
        i, j, minDiff = 0, m - 1, float('inf')
        indexes = [0, 0]

        while i < n and j >= 0:
            sumVal = arr[i] + brr[j]
            diff = abs(sumVal - x)

            if minDiff > diff:
                indexes[0] = arr[i]
                indexes[1] = brr[j]
                minDiff = diff

            if sumVal < x:
                i += 1
            else:
                j -= 1
        return indexes
