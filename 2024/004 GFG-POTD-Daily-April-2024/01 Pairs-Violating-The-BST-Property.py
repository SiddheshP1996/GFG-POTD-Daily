# User function template for Python

from typing import Optional
from collections import deque
from bisect import bisect_right

"""
# definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def pairsViolatingBST(self, n : int, root : Optional['Node']) -> int:
        # Code here
        inorder = []

        def execute_pairsBST(root):
            if not root:
                return
            execute_pairsBST(root.left)
            inorder.append(root.data)
            execute_pairsBST(root.right)

        execute_pairsBST(root)
        if len(inorder) <= 1:
            return 0

        pairs_queue = []
        for i, val in enumerate(inorder):
            pairs_queue.append((val, i))
        pairs_queue.sort()

        result = 0
        x = []
        while pairs_queue:
            val, i = pairs_queue.pop(0)
            count = bisect_right(x, i)
            result += i - count
            x.insert(count, i)

        return result
