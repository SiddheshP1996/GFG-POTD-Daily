# User function Template for python3

class Solution:
    def sortedInsert(self, head1, key):
        # code here
        # return head of edited linked list
        new_node = Node(key)
        curr = head1
        if key < curr.data:
            new_node.next = curr
            return new_node
        while curr.next and key > curr.next.data:
            curr = curr.next
        temp = curr.next
        curr.next = new_node
        new_node.next = temp
        return head1
