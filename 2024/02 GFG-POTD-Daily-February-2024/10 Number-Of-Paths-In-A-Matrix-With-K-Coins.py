# User function Template for python3

class Solution:
    def numberOfPath (self, n, k, arr):
        # Code here
        def executeMatrixPath(rows, columns, n, k, arr, dp):
            if rows == n - 1 and columns == n - 1 and k == arr[rows][columns]:
                return 1
            if rows >= n or columns >= n or k < 0:
                return 0
            if dp[rows][columns][k] != -1:
                return dp[rows][columns][k]
            matrix = executeMatrixPath(rows + 1, columns, n, k - arr[rows][columns], arr, dp)
            result = executeMatrixPath(rows, columns + 1, n, k - arr[rows][columns], arr, dp)
            dp[rows][columns][k] = matrix + result
            return dp[rows][columns][k]
        
        dp=[[[-1 for element in range(k + 1)] for element in range(n + 1)] for element in range(n + 1)] 
        return executeMatrixPath(0, 0, n, k, arr, dp)