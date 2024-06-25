# User function Template for python3

"""
  reverse alternate nodes and append at the end
  The input list will have at least one element
  Node is defined as
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

"""


class Solution:
    def rearrange(self, head):
        # Code here
        prev = head
        current = head.next
        new_tail = Node(-1)
        tail_pointer = new_tail
        while current is not None:
            next = current.next
            current.next = None
            tail_pointer.next = current
            tail_pointer = tail_pointer.next
            prev.next = next
            if next is None:
                current = None
            else:
                prev = prev.next
                current = next.next

        def rev(h):
            if h is None:
                return h
            prev = None
            current = h
            next = h.next

            while current is not None:
                current.next = prev
                prev = current
                current = next
                if next is not None:
                    next = next.next
            return prev

        new_tail = new_tail.next

        prev.next = rev(new_tail)
        return head
