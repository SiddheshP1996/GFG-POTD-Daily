# User function Template for python3


from typing import List


class Solution:
    def printGraph(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        # code here
        adjacency_list = [[] for _ in range(V)]

        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        return adjacency_list
