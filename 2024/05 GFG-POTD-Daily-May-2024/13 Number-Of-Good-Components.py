# User function Template for python3

from typing import List
from collections import defaultdict

class Solution:
    def findNumberOfGoodComponent(self, e : int, v : int, edges : List[List[int]]) -> int:
        # Code here
        checkParent = list(range(v))
        
        def find(x: int) -> int:
            if checkParent[x]==x:
                return x
            checkParent[x] = find(checkParent[x])
            return checkParent[x]
        
        degreeOfVertices = [0] * v
        for x, y in edges:
            degreeOfVertices[x - 1] += 1
            degreeOfVertices[y - 1] += 1
            checkParent[find(x - 1)] = find(y - 1)
        group = defaultdict(list)
        for i in range(v): 
            group[find(i)].append(i)
        return sum(all(degreeOfVertices[x] == len(components) - 1 for x in components) for components in group.values())
