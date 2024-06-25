# Your task is to complete this function
# Function should return an integer value

"""
class node:
    def __init__(self):
        self.data = None
        self.next = None
"""

class Solution:
    def decimalValue(self, head):
        mod = ((10**9) + 7)
        # Code here
        # Initialize the result variable to store the decimal value
        decimal_value = 0

        # Traverse the binary linked list
        while head:
            # Update the result by left-shifting and adding the current binary digit
            decimal_value = (decimal_value * 2 + head.data) % mod
            # Move to the next node in the linked list
            head = head.next

        # Return the final decimal value
        return decimal_value
