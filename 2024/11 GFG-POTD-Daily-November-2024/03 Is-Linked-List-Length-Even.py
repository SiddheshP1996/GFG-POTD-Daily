# User function Template for python3

class Solution:
    # Your task is to complete this function
    # Function should return false if length is even
    # else return true
    def isLengthEven(self, head):
        # Code here
        count = 0
        headPointer = head
        while headPointer != None:
            count += 1
            headPointer = headPointer.next
        if count % 2 == 0:
            return True
        else:
            return False
