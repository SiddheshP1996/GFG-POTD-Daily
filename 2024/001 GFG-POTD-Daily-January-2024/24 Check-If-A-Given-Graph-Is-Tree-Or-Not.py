# User function Template for python3

class Solution:
    def dfs(self, adjacent, starting_vertex):
        n = len(adjacent)
        visited = [False] * n
        stack = [(starting_vertex, -1)]
        visited[starting_vertex] = True
        while stack:
            current_vertex, parent = stack.pop()
            for visit in adjacent[current_vertex]:
                if visited[visit] == False:
                    stack.append((visit, current_vertex))
                    visited[visit] = True
                elif visit != parent:
                    return 0
        if False in visited:
            return 0
        return 1
        
    def isTree(self, n, m, edges):
        # Code here
        adjacent = [[] for item in range(n)]
        for e in edges:
            adjacent[e[0]].append(e[1])
            adjacent[e[1]].append(e[0])
        return self.dfs(adjacent, 0)
