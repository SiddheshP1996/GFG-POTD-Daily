# User function Template for python3

"""  
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""

class Solution:
    def count(self, head, key):
        # Code here
        result = 0
        while head:
            if head.data == key:
                result += 1
            head = head.next
        return result
