# User function Template for python3

class Solution:
    def fill(self, n, m, mat):
        # code here
        if not mat:
            return mat
        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or mat[r][c] != 'O':
                return
            mat[r][c] = 'V'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for i in range(n):
            if mat[i][0] == 'O':
                dfs(i, 0)
            if mat[i][m - 1] == 'O':
                dfs(i, m - 1)
        for j in range(m):
            if mat[0][j] == 'O':
                dfs(0, j)
            if mat[n - 1][j] == 'O':
                dfs(n - 1, j)
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 'O':
                    mat[i][j] = 'X'
                elif mat[i][j] == 'V':
                    mat[i][j] = 'O'
        return mat
