# User function Template for python3

from typing import List


class Solution:
    def minimumEdgeRemove(self, n : int, edges : List[List[int]]) -> int:
        # Code here
        def execute(node, parent, adjacentNode, sizeOfSubTree, removableEdges):
            nodeCount = 1
            for neighbor in adjacentNode[node]:
                if neighbor != parent:
                    nodeCount += execute(neighbor, node, adjacentNode, sizeOfSubTree, removableEdges)
            sizeOfSubTree[node] = nodeCount
            if nodeCount % 2 == 0 and node != 1:
                removableEdges.append((parent, node))
            return nodeCount
        
        adjacentNode = {i: [] for i in range(1, n + 1)}
        for u, v in edges:
            adjacentNode[u].append(v)
            adjacentNode[v].append(u)
        sizeOfSubTree = [0] * (n + 1)
        removableEdges = []

        execute(1, -1, adjacentNode, sizeOfSubTree, removableEdges)
    
        return len(removableEdges)
