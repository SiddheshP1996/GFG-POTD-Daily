# User function Template for python3

"""
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
"""

class Solution():
# Function to sort the given doubly linked list using Merge Sort.
    def sortDoubly(self, head):
        # Your code here
        numList = []
        while head:
            numList.append(head.data)
            head = head.next
        numList.sort()
        root = Node(numList[0])
        currentNode = root
        for i in numList[1:]:
            currentNode.next = Node(i)
            currentNode.next.prev = currentNode
            currentNode = currentNode.next
        return root
