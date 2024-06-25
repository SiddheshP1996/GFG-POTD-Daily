# User function template for Python

"""
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
"""

class Solution:
    def absolute_diff(self, root):
        # Your code here
        result = float('inf')
        stack = []
        current = root
        previous = None
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            
            if previous:
                result = min(result, abs(previous.data - current.data))
            previous = current
            current = current.right
        return result
