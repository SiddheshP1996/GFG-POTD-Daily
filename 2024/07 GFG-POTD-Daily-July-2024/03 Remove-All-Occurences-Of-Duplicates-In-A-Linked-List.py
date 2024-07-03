# User function Template for python3

"""
# Linked list Node class

    class Node :
        def __init__(self, val):
            self.data = val
            self.next = None

"""

class Solution:
    def removeAllDuplicates(self, head):
        # Code here
        dummyNode = Node(0)
        dummyNode.next = head
        previousNode = dummyNode
        currentNode = head

        while currentNode:
            while currentNode.next and currentNode.data == currentNode.next.data:
                currentNode = currentNode.next

            if previousNode.next == currentNode:
                previousNode = previousNode.next
            else:
                previousNode.next = currentNode.next
            
            currentNode = currentNode.next

        return dummyNode.next
