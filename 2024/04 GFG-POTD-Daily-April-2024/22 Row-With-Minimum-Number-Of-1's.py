# User function Template for python3

class Solution:
    def minRow(self, n, m, a):
        # Code here
        rows = sum(a[0])
        m = 0 
        
        for i in range(n):
            totalRows = sum(a[i])
            if totalRows < rows:
                rows = totalRows
                m = i
        return m + 1
