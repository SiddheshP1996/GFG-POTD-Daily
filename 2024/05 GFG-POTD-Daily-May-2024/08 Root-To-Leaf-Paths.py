# User function TemporaryRootStorelate for python3

from typing import Optional
from collections import deque

from typing import List

"""
definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        # Code here
        result = []
        def execute(root, rootStore):
            temporaryRootStore = rootStore
            if root is None:
                return
            temporaryRootStore.append(root.data)
            if not root.left and not root.right:
                result.append(temporaryRootStore[:])
                temporaryRootStore.pop()
                return
            execute(root.left, temporaryRootStore)
            execute(root.right, temporaryRootStore)
            temporaryRootStore.pop()
        execute(root, [])
        return result
