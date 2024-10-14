# User function Template for python3

"""
# Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
"""

class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # Code here
        count = 0
        iteration = head
        while iteration.next != None:
            count += 1
            iteration = iteration.next
        return count + 1
