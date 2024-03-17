# User function Template for python3

"""
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
"""

class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        """
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        """
        dic = dict()
        count = 0
        
        while head1:
            dic[x -  head1.data] = dic.get(x - head1.data, 0) + 1
            head1 = head1.next
        
        while head2:
            count += dic.get(head2.data, 0)
            head2 = head2.next
        return count
