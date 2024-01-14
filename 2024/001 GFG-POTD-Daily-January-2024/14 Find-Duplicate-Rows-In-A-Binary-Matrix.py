# User function Template for python3

# Solution 1

class Solution:
    def repeatedRows(self, arr, m ,n):
        # Code here
        setOfRows = set()
        result = []
        for i in range(m):
            rowsInMatrix = 0
            for item in arr[i]:
                rowsInMatrix = (rowsInMatrix << 1) + item
            if rowsInMatrix in setOfRows:
                result.append(i)
            else:
                setOfRows.add(rowsInMatrix)
        return result

# Solution 2

class Solution:
    def repeatedRows(self, arr, m ,n):
        #code here
        repeatedNumberOfRows = []
        for i in range(1, m):
            if arr[i] in arr[:i]:
                repeatedNumberOfRows.append(i)
        return repeatedNumberOfRows
