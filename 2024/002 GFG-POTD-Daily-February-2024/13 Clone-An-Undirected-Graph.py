# User function Template for python3

"""
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

from sys import setrecursionlimit

class Solution():
    def cloneGraph(self, node):
        # Your code goes here
        setrecursionlimit(10**4)
        correctCopy = dict()
        qForBFS = [node]
        while qForBFS:
            currentElement = qForBFS.pop()
            correctCopy[currentElement] = Node()
            for next in currentElement.neighbors:
                if next not in correctCopy:
                    qForBFS.append(next)
        for originalNode, correspondingNodeCopy in correctCopy.items():
            correspondingNodeCopy.val = originalNode.val
            correspondingNodeCopy.neighbors = [correctCopy[x] for x in originalNode.neighbors]
        return correctCopy[node]
