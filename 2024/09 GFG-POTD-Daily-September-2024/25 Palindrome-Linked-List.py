# User function Template for python3

"""
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
"""

# Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        # Code here
        if not head or not head.next:
            return True
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        previousHead, currentHead = None, slow
        while currentHead:
            currentHead.next, previousHead, currentHead\
                = previousHead, currentHead, currentHead.next
        
        firstHalf, secondHalf = head, previousHead
        while secondHalf:
            if firstHalf.data != secondHalf.data:
                return False
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        
        return True
