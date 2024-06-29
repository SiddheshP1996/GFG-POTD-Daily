# Your task is to complete this function
# Function should return true/1 if both
# Are identical else return false/0
"""
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
"""

# Function to check whether two linked lists are identical or not.
def areIdentical(head1, head2):
    # Code here
    while head1 and head2:
        if head1.data!=head2.data:
            return False
        head1 = head1.next
        head2 = head2.next
    if head1 or head2:
        return False
    return True
