# User function Template for python3

"""
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
"""

class Solution:
    def reverse(self, head):
        currentHead = head
        previousHead = None
        while currentHead:
            temporaryHead = currentHead.next
            currentHead.next = previousHead
            previousHead = currentHead
            currentHead = temporaryHead
        return previousHead
    
    def addOne(self, head):
        #Returns new head of linked List.
        head = self.reverse(head)
        currentHead = head
        previousHead = None
        while currentHead and currentHead.data == 9:
            currentHead.data = 0
            previousHead = currentHead
            currentHead = currentHead.next
            
        if currentHead:
            currentHead.data += 1
        else:
            previousHead.next = Node(1)
            
        head = self.reverse(head)
        return head
