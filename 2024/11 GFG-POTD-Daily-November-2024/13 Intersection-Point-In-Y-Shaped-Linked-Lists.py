# User function Template for python3
"""
	Function to return the value at point of intersection
	in two linked list, connected in y shaped form.
	
	Function Arguments: head_a, head_b (heads of both the lists)
	
	Return Type: value in NODE present at the point of intersection
	             or -1 if no common point.

	Contributed By: Nagendra Jha

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
"""

# Function to find intersection point in Y shaped Linked Lists.

def getLength(root):
    count = 0
    temp = root
    while temp != None:
        temp = temp.next
        count += 1
    
    return count
    
def intersetPoint(head1, head2):
    # Code here
    lengthOne, lengthTwo = getLength(head1), getLength(head2)
    
    if lengthOne < lengthTwo:
        head1, head2 = head2, head1
        lengthOne, lengthTwo = lengthTwo, lengthOne
    
    diff = lengthOne - lengthTwo    
    pointer1, pointer2 = head1, head2
    
    while diff > 0:
        pointer1 = pointer1.next
        diff -= 1
    
    while pointer1 != None:
        if pointer1 == pointer2:
            return pointer1.data
        
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    return -1
