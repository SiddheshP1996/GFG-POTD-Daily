# Your task is to complete this function

"""
class node:
    def __init__(data):
        self.data = data
        self.next = None
"""
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        if head is None:
            return -1
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
