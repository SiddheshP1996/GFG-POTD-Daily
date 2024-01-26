# User function Template for python3

class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w
        
class Solution:    
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W, arr, n):
        # Code here
        arr.sort(key=lambda item: item.value/item.weight, reverse = True)
        items, result = 0, 0
        while items < n and W >= arr[items].weight:
            result += arr[items].value
            W -= arr[items].weight
            items += 1
        if items < n:
            result += (W / arr[items].weight) * arr[items].value
        return result
