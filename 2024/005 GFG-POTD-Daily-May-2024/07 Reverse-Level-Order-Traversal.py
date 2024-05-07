# User function Template for python3

from collections import deque

"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

def reverseLevelOrder(root):
    # Code here
    result = deque()
    que = deque()
    que.append(root)
    while que:
        node = que.popleft()
        result.appendleft(node.data)
        if node.right:
            que.append(node.right)
        if node.left:
            que.append(node.left)
    return result
