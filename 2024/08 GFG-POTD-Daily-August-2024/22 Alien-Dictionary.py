# User function Template for python3

from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
        # Your implementation here
        adjacent = defaultdict(set)
        inDegree = defaultdict(int)
        character = set()
        for index, value in enumerate(alien_dict):
            if index + 1 == n:
                continue
            
            currentElement = list(value)
            nextElement = list(alien_dict[index + 1])
            character.update(currentElement + nextElement)
            
            for a, b in zip(currentElement, nextElement):
                if a == b:
                    continue
                
                if b not in adjacent[a]:
                    inDegree[b] += 1
                    adjacent[a].add(b)
                break
            
        queue = []
        for c in character:
            if inDegree[c] == 0:
                queue.append(c)
                
        queueReturn = []
        while queue:
            currentElement = queue.pop()
            queueReturn.append(currentElement)
            for nextElement in adjacent[currentElement]:
                inDegree[nextElement] -= 1
                if inDegree[nextElement] == 0:
                    queue.append(nextElement)
        return queueReturn
