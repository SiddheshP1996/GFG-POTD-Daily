# User function Template for python3

class Solution:
    def subLinkedList(self, l1, l2): 
        # Code here
        # Return head of difference list
        string_1, string_2 = '', ''
        while l1:
            string_1 += str(l1.data)
            l1 = l1.next
        while l2:
            string_2 += str(l2.data)
            l2 = l2.next
        number_1, number_2 = int(string_1), int(string_2)
        return Node(abs(number_1 - number_2))
