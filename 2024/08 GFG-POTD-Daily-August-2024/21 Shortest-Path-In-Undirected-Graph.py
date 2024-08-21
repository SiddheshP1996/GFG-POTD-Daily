# User function Template for python3

from collections import deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        # Code here
        adjacentList = [[] for elements in range(n)]
        
        for leftEdge, rightEdge in edges:
            adjacentList[leftEdge].append(rightEdge)
            adjacentList[rightEdge].append(leftEdge)
            
        distance = [float('inf')] * n
        distance[src] = 0
        
        queue = deque([src])
        
        while queue:
            node = queue.popleft()
            for neighborNode in adjacentList[node]:
                if distance[neighborNode] == float('inf'):
                    distance[neighborNode] = distance[node] + 1
                    queue.append(neighborNode)
                    
        distance = [-1 if dist == float('inf') else dist for dist in distance]
        
        return distance
