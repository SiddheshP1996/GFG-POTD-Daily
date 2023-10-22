# User function Template for python3

from typing import List


class Solution:
    def eventualSafeNodes(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        def isSafe(node, visited):
            # If the node has been visited and marked safe before, return True
            if visited[node] == 1:
                return True
            # If the node has been visited and marked unsafe before, return False
            if visited[node] == -1:
                return False
            visited[node] = -1  # Mark the node as unsafe
            # Recursively check all neighbors
            for neighbor in adj[node]:
                if not isSafe(neighbor, visited):
                    return False
            visited[node] = 1  # Mark the node as safe
            return True
        # Initialize an array to keep track of visited nodes.
        visited = [0] * V
        result = []
        # Start DFS from each node
        for node in range(V):
            if isSafe(node, visited):
                result.append(node)
        return sorted(result)
