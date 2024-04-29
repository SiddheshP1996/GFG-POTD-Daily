# Your task is to complete this function
# Your function should return the new head pointer

"""
class node:
    def __init__(self,x):
        self.data = x
        self.next = None
"""

class Solution:
    def deleteK(self, head, k):
        # Code here
        if k == 1:
            return None
        
        count, currentNode = 1, head
        
        while currentNode:
            if count == k - 1 and currentNode.next:
                currentNode.next = currentNode.next.next
                count = 0
                
            count, currentNode = count + 1, currentNode.next
            
        return head
