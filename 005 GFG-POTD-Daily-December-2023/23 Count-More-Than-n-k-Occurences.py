# User function Template for python3


class Solution:
    
    # Function to find all elements in array that appear more than n/k times.
    def countOccurence(self, arr, n, k):
        # Your code here
        dictionaryElements = {}
        countStorage = 0
        for i in arr:
            if i not in dictionaryElements:
                dictionaryElements[i] = 1
            else:
                dictionaryElements[i] += 1
        for i, j in dictionaryElements.items():
            if j > n // k:
                countStorage += 1
        return countStorage
