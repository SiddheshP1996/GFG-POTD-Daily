# Your task is to complete this function

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""

class Solution:
    
    # Function to rotate a linked list.
    def rotateList(self, listHead, tail):
        headPoint = listHead
        listHead = listHead.next
        headPoint.next = None
        tail.next = headPoint
        return listHead, tail.next
        
    def rotate(self, head, k):
        # Code here
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        k = k % n
        
        for i in range(k):
            head, tail = self.rotateList(head, tail)
        return head
