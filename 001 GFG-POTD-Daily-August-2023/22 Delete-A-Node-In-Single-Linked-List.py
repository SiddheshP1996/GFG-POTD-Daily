# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''


def delNode(head, k):
    # Code here
    if not head:
        return None
    c = 1
    if k == c:
        return head.next

    temp = head
    while temp:
        if c + 1 == k:
            temp.next = temp.next.next
        c += 1
        temp = temp.next
    return head