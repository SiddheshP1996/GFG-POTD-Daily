# User function Template for python3

class Solution:
    def delete_node(self, head, x):
        # Code here
        l = head
        i = 1
        while head != None:
            if i == x:
                n = head.next
                p = head.prev
                if p != None:
                    p.next = n
                else:
                    l = n
                break
            i += 1
            head = head.next
        return l
