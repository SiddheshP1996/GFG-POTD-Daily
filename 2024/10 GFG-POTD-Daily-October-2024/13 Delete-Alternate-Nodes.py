# User function Template for python3

"""
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None
"""

class Solution:
    def deleteAlt(self, head):
        # Code here
        while head != None and head.next != None:
            head.next = head.next.next
            head = head.next
