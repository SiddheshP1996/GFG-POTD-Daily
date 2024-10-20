# User function Template for python3

from heapq import heappush, heappop

"""
class DLLNode:
    def __init__(self,val) -> None:
        self.data = val
        self.prev = None
        self.next = None
"""

class Solution:
    def sortAKSortedDLL(self, head, k):
        # Code Here
        priorityQueue = []
        temp = head
        
        for i in range(k + 1):
            heappush(priorityQueue, temp.data)
            temp = temp.next
            
        tail = head
        while priorityQueue:
            tail.data = heappop(priorityQueue)
            if temp:
                heappush(priorityQueue, temp.data)
                temp = temp.next
            tail = tail.next
        return head
