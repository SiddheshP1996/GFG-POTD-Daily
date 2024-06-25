# User function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    # Function to reverse a linked list.
    vowels = ['a', 'e', 'i', 'o', 'u']
    def arrangeCV(self, head):
        # Code here
        currentNode = head
        vowelHead, vowelTail = None, None
        consonentHead, consonentTail = None, None

        while currentNode:
            if currentNode.data in self.vowels:
                if vowelHead:
                    vowelTail.next = currentNode
                else:
                    vowelHead = currentNode
                vowelTail = currentNode

            else:
                if consonentHead:
                    consonentTail.next = currentNode
                else:
                    consonentHead = currentNode
                consonentTail = currentNode
            currentNode = currentNode.next

        if consonentTail:
            consonentTail.next = None

        if vowelTail:
            vowelTail.next = consonentHead
        return vowelHead if vowelHead else consonentHead