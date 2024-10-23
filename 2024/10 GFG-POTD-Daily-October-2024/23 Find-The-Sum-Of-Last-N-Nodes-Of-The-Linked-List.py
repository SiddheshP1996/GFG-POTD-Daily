# User function Template for python3

"""
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
"""

class Solution:
    def sumOfLastN_Nodes(self, head, n):
        # Function should return sum of last n nodes
        nodeSum = 0
        count = 0
        currentHead = head
        temp = head
        while temp!= None:
            nodeSum += temp.data
            count += 1
            if count > n:
                nodeSum -= currentHead.data
                currentHead = currentHead.next
                count -= 1
            temp = temp.next
        return nodeSum
