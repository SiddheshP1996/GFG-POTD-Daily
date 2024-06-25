# User function Template for python3

"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
"""

class Solution:
    def mergeResult(self, h1, h2):
        # Return head of merged list
        arr = []
        
        # Write a function that will take the head of the linked list and append all the data to an array
        def appendFunc(head):
            while head:
                arr.append(head.data)
                head = head.next
        
        # append both linked lists to the array
        appendFunc(h1)
        appendFunc(h2)
        
        # reverse sort the array in-place
        arr.sort(reverse = True)
        
        # create a dummyListStorage node to simplify linked list creation
        dummyListStorage = Node(0)
        currentNode = dummyListStorage
        
        # iterate over the sorted array to create  the linked list
        for value in arr:
            currentNode.next = Node(value)
            currentNode = currentNode.next
            
        return dummyListStorage.next
