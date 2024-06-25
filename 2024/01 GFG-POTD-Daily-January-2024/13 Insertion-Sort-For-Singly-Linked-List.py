# User function Template for python3

"""
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
"""

class Solution:
    def insertionSort(self, head):
        # Code here
        dummyNode = Node(-1)
        dummyNode.next = head
        temporaryNode = head
        previousNode = head
        temporaryNode = temporaryNode.next

        while(temporaryNode != None):
        
            if temporaryNode.data < previousNode.data:
                previousNode2 = dummyNode
                temporaryNode2 = dummyNode.next
        
                while(temporaryNode2.data < temporaryNode.data):
                    temporaryNode2 = temporaryNode2.next
                    previousNode2 = previousNode2.next
        
                previousNode.next = temporaryNode.next
                previousNode2.next = temporaryNode
                temporaryNode.next = temporaryNode2
                temporaryNode = previousNode.next
        
            else:
                previousNode = previousNode.next
                temporaryNode = temporaryNode.next
        
        return dummyNode.next
