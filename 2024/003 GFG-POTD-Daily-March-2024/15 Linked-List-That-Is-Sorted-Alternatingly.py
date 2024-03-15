#User function Template for python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sort(self, h1):
        #return head
        arr = []
        new = h1
        while new:
            arr.append(new.data)
            new = new.next
        sortedArr = sorted(arr)
        for i in range(len(sortedArr)):
            print(sortedArr[i], end=" ")