# User function Template for python3

from typing import List


class Solution:
    def vertexCover(self, n : int, edges : List[List[int]]) -> int:
        # Code here
        def solve(edges):
            if len(edges) == 0:
                return 0
            edge0 = []
            edge1 = []
            for i in edges:
                if not(i[0] == edges[0][0] or i[1] == edges[0][0]):
                    edge0.append(i)
                if not(i[0] == edges[0][1] or i[1] == edges[0][1]):
                    edge1.append(i)
            result0 = 1 + solve(edge0)
            result1 = 1 + solve(edge1)
            return min(result0, result1)
            
        return solve(edges)
