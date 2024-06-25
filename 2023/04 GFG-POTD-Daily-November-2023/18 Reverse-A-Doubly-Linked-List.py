# User function Template for python3

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
"""


class Solution:
    def reverseDLL(self, head):
        # return head after reversing
        pointerOne = head
        pointerTwo = None

        while pointerOne is not None:
            nextPointerData = pointerOne.next
            pointerOne.next = pointerTwo
            pointerOne.prev = nextPointerData

            pointerTwo = pointerOne
            pointerOne = nextPointerData

        return pointerTwo
