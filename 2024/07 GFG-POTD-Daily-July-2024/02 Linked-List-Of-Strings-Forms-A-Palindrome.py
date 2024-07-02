# User function Template for python3

"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
"""

def compute(head): 
    # Return True/False
    isPalindromeString = ''
    while head:
        isPalindromeString += head.data
        head = head.next
    return isPalindromeString == (isPalindromeString[::-1])
