# User function Template for python3

"""
# Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""
class Solution:
    # Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        # code here
        # return head of sum list
        t1, t2 = num1, num2
        x, y="", ""
        while t1:
            x += str(t1.data)
            t1 = t1.next
        while t2:
            y += str(t2.data)
            t2 = t2.next
        n1, n2=int(x), int(y)
        result = n1 + n2
        w = LinkedList()
        resultList = []
        if result == 0:
            resultList = [0]
        while result > 0:
            resultList.append(result % 10)
            result //= 10
        resultList = resultList[::-1]
        for i in resultList:
            w.insert(i)
        return w.head
