# User function Template for python3

from collections import defaultdict

class Solution:
    def findOrder(self, n, m, prerequisites):
        # Code here
        graph_of_task_order = defaultdict(list)
        for num1, num2 in prerequisites: graph_of_task_order[num1].append(num2)
        result, visited = [], [0] * n
        def dfs(i):
            if visited[i]: return visited[i] == 1
            visited[i] = -1
            if any(not dfs(node) for node in graph_of_task_order[i]): return False
            visited[i] = 1
            result.append(i)
            return True
        return all(dfs(node) for node in range(n)) and result or []
