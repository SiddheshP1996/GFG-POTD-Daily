# User function Temporary_nodelate for python3

"""
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
"""

class Solution:
    def sortedInsert(self, head, data):
        # Code here
        if not head:
            temporary_node = Node(data)
            temporary_node.next = temporary_node
            return temporary_node
        if head.data > data:
            temporary_node = Node(head.data)
            temporary_node.next = head.next
            head.next = temporary_node
            head.data = data
        else:
            current_node = head
            while current_node.next != head and current_node.next.data < data:
                current_node = current_node.next
            temporary_node = Node(data)
            temporary_node.next = current_node.next
            current_node.next = temporary_node
        return head
