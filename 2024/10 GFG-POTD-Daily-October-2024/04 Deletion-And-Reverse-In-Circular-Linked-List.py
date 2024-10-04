# User function Template for python3

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""

class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        # Code here
        previousHead = head
        currentHead = head.next
        
        while 1:
            tempHead = currentHead.next
            currentHead.next = previousHead
            previousHead = currentHead
            currentHead = tempHead
            
            if previousHead == head:
                break
            
        return head.next
        
    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        # Code here
        previousHead = head
        currentHead = previousHead.next
        
        while currentHead != head:
            previousHead = currentHead
            currentHead = currentHead.next
            
        while 1:
            if currentHead.data == key:
                previousHead.next = currentHead.next
                if currentHead == head:
                    head = head.next
                del currentHead
                break
            
            previousHead = currentHead
            currentHead = currentHead.next
            
            if currentHead == head:
                break
            
        return head
