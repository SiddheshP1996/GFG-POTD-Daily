# User function Template for python3

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""

class Solution:
    def deleteMid(self, head):
        """
        head:  head of given linkedList
        return: head of resultant llist
        """
        # Code here
        if not head.next:
            return None
        
        fastPointer = head.next.next
        slowPointer = head
        
        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        
        slowPointer.next = slowPointer.next.next
        return head
