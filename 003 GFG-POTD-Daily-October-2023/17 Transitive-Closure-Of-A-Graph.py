# User function Template for python3

class Solution:
    def transitiveClosure(self, N, graph):
        # code here
        tc = [[0] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if i == j or graph[i][j] == 1:
                    tc[i][j] = 1

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    tc[i][j] = tc[i][j] or (tc[i][k] and tc[k][j])

        return tc
