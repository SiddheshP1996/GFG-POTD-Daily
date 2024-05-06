# User function Template for python3

"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

def noSibling(root):
    # Code here
    resultList = []
    stack = [(root, 1)]
    
    while stack:
        node, siblings = stack.pop()
        
        if not siblings:
            resultList.append(node.data)
        
        siblings = 1 if node.right and node.left else 0
        for child in [node.right, node.left]:
            if child:
                stack.append((child, siblings))
    
    return sorted(resultList) if resultList else [-1]
