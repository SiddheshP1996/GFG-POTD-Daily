# User function Template for python3

from heapq import heappush, heappush, heappop

class Solution:
    def printKClosest(self, arr, n, k, x):
        # Code here
        priorityQueue = []
        
        for item in range(n):
            if arr[item] == x:
                continue
            
            heappush(priorityQueue, (-abs(arr[item] - x), item))
            
            if len(priorityQueue) > k:
                heappop(priorityQueue)
            
        result = [-1] * k
            
        for item in range(k):
            _, index = heappop(priorityQueue)
            
            result[k - item - 1] = arr[index]
            
        return result
