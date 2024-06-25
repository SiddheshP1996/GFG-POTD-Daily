# User function Template for python3

"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    # Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        # Add Your code here
        queue = [[root]]
        result = []
        checker = False
        while len(queue) != 0:
            temp = queue.pop()
            nodes = []
            value = []
            for currentNode in temp:
                value.append(currentNode.data)
                if currentNode.left:
                    nodes.append(currentNode.left)
                
                if currentNode.right:
                    nodes.append(currentNode.right)
                    
            if len(nodes) > 0:
                queue.append(nodes)
                
            if checker:
                result.extend(value[::-1])
                checker = False
                continue
            
            checker = True
            result.extend(value)
            
        return result
