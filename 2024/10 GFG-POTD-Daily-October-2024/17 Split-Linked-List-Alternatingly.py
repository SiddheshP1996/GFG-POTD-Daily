# User function Template for python3

"""
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
"""

class Solution:
    def alternatingSplitList(self, head):
        # Your code here
        d1 = c1 = Node(0)
        d2 = c2 = Node(0)
        currentHead = head
        count = 1
        while currentHead:
            if (count % 2 != 0):
                c1.next = currentHead
                c1 = c1.next
                tempHead1 = c1
            else:
                c2.next = currentHead
                c2 = c2.next
                tempHead2 = c2
         
            count += 1
            currentHead = currentHead.next
        tempHead1.next = None
        tempHead2.next = None
        return [d1.next, d2.next]
