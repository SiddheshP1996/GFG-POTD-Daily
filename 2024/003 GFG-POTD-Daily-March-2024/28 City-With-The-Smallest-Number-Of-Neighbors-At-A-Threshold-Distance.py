# User function Template for python3

import heapq
from typing import List

class Solution:
    def findCity(self, n : int, m : int, edges : List[List[int]], distanceanceThreshold : int) -> int:
        # Code here
        graph = [[] for _ in range(n)]
        
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
            
        def getNeighborsCount(city):
            heap = [(0, city)]
            distance = {}
            
            while heap:
                currentWeight, u = heapq.heappop(heap)
                if u in distance:
                    continue
                if u != city:    
                    distance[u] = currentWeight
                for v, weight in graph[u]:
                    if v in distance:
                        continue
                    if currentWeight + weight <= distanceThreshold:
                        heapq.heappush(heap, (currentWeight + weight, v))
            return len(distance)
        
        return max([(getNeighborsCount(city), city) for city in range(n)], key=lambda x: (-x[0], x[1]))[-1]
