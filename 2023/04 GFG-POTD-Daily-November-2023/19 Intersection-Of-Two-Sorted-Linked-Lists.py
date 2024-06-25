# User function Template for python3

"""
structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

"""


class Solution:
    def findIntersection(self, head1, head2):
        # return head
        intersectionPointOfList = linkedList()

        while head1 and head2:
            if head1.data == head2.data:
                intersectionPointOfList.insert(head1.data)
                head1, head2 = head1.next, head2.next

            elif head1.data < head2.data:
                head1 = head1.next

            else:
                head2 = head2.next

        return intersectionPointOfList.head
