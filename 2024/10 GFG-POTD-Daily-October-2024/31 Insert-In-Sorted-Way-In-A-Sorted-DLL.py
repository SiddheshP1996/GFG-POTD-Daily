# User function Template for python3

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
"""

class Solution:
    # Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        # Code here
        currentHead = head
        emptyList = []
        while(currentHead):
            emptyList.append(currentHead.data)
            currentHead = currentHead.next
        emptyList.append(x)
        emptyList.sort()
        for i in (emptyList):
            print(i, end=" ")
