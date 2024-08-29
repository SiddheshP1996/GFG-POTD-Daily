# User function Template for python3

"""
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

"""

class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        # Your code here
        leftNode = rightNode = head
        while rightNode and rightNode.next:
            leftNode = leftNode.next
            rightNode = rightNode.next.next
            
            if leftNode == rightNode:
                count = 1
                while leftNode.next != rightNode:
                    count += 1
                    leftNode = leftNode.next
                return count
        return 0
