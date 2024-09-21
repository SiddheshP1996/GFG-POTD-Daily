# User function Template for python3

"""
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.random=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
"""

class Solution:
    # Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # Code here
        if not head:
            return None
        
        cloneDict = {}
        currentHead = head
        while currentHead:
            cloneDict[currentHead] = Node(currentHead.data)
            currentHead=currentHead.next
            
        currentHead = head
        while currentHead:
            cloneDict[currentHead].next = cloneDict.get(currentHead.next)
            cloneDict[currentHead].random = cloneDict.get(currentHead.random)
            currentHead = currentHead.next
            
        return cloneDict[head]
