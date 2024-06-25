# User function Template for python3

'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''


class Solution:
    def compute(self, head):
        # Your code here
        if not head or not head.next:
            return head

        ptr = head
        while ptr.next and ptr:
            if ptr.data < ptr.next.data:
                ptr.data = ptr.next.data
                ptr.next = ptr.next.next
                ptr = head
            else:
                ptr = ptr.next

        return head