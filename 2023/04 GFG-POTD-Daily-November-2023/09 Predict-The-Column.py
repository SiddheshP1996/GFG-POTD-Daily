# User function Template for python3

class Solution:
    def columnWithMaxZeros(self, arr, N):
        # code here
        countColumns = [0] * N
        for i in range(N):
            for j in range(N):
                countColumns[j] += ((arr[i][j] + 1) % 2)
        columnNumber = -1
        for i in range(N):
            if countColumns[i] > 0 and columnNumber == -1:
                columnNumber = i
            elif countColumns[i] > countColumns[columnNumber]:
                columnNumber = i
        return columnNumber
