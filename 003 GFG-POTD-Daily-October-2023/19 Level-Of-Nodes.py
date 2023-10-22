# User function Template for python3

import collections


class Solution:

    # Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        # code here
        q = collections.deque()
        adj_list = collections.defaultdict(list)
        found = False
        for u in range(V):
            neigh = adj[u]
            for j in neigh:
                if u == X or j == X:
                    found = True
                adj_list[u].append(j)
                adj_list[j].append(u)

        if not found:
            return -1

        q.append(0)
        visited = set()
        level = 0
        while len(q) > 0:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node == X:
                    return level
                visited.add(node)
                for neigh in adj_list[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)
            level += 1
        return -1
