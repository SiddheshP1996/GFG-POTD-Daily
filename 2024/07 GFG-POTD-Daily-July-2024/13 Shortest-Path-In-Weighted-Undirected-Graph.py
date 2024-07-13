# User function Template for python3

from typing import List
from heapq import heappop, heappush

class Solution:
    def shortestPath(self, n:int, m:int, edges:List[List[int]] )->List[int]:
        # Code here
        adj = [[] for _ in range(n + 1)]
        for sourceNode, distanceNode, edgeWeight in edges:
            adj[sourceNode].append((distanceNode, edgeWeight))
            adj[distanceNode].append((sourceNode, edgeWeight))
            
        numberOfVertices = n
        startNode = 1
        destination = numberOfVertices
        
        parent = [i for i in range(numberOfVertices + 1)]
        path = []
        priorityQueue = []
        
        distance = [float('inf')] * (numberOfVertices + 1)
        distance[startNode] = 0
        parent[startNode] = startNode
        heappush(priorityQueue, (0, startNode))

        while priorityQueue:
            dis, node = heappop(priorityQueue)
            for adjacentNode, wt in adj[node]:
                if dis + wt < distance[adjacentNode]:
                    distance[adjacentNode] = dis + wt
                    heappush(priorityQueue, (distance[adjacentNode], adjacentNode))
                    parent[adjacentNode] = node

        node = destination
        while parent[node] != node:
            path.append(node)
            node = parent[node]
            
        if distance[destination] == float('inf'):
            return [-1]
        
        path.append(startNode)
        totalDistance = distance[destination]
        return [totalDistance] + path[::-1]
