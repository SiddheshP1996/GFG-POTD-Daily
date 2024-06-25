"""  list Node is as defined below:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""


# complete this function
# return head of list after swapping
class Solution:
    def pairWiseSwap(self, head):
        # code here
        """
        temp = head
        while temp and temp.next:
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next
        return head
        """
        # Check if the list has at least two nodes
        if head is None or head.next is None:
            return head

        # Initialize the pointers for swapping
        prevNode = None
        currentNode = head

        # Traverse and swap pairs of nodes
        while currentNode is not None and currentNode.next is not None:
            # Nodes to be swapped
            firstNode = currentNode
            secondNode = currentNode.next

            # Swap the nodes
            firstNode.next = secondNode.next
            secondNode.next = firstNode

            if prevNode is None:
                # Update the new head of the list
                head = secondNode
            else:
                # Link the previous node to the swapped pair
                prevNode.next = secondNode

            # Move the pointers for the next iteration
            prevNode = firstNode
            currentNode = firstNode.next

        return head
