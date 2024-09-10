# User function Template for python3

from collections import defaultdict, Counter

class Solution:
    def isCircle(self, arr):
        # Code here
        g = defaultdict(list)
        inDegree = Counter()
        outDegree = Counter()
        for s in arr:
            g[s[0]].append(s[-1])
            inDegree[s[-1]] += 1
            outDegree[s[0]] += 1
        
        if inDegree != outDegree:
            return 0
        
        visited = set()
        def dfs(n, g):
            if n in visited:
                return
            visited.add(n)
            for neighbour in g[n]:
                dfs(neighbour, g)
        
        dfs(arr[0][0], g)
        if len(visited) != len(g):
            return 0
        return 1
