# User function Template for python3

from collections import Counter

class Solution:
   
    # Function to sort the array according to frequency of elements.
    def sortByFreq(self, arr):
        # Code here
        frequency = Counter(arr)
        sortedArray = sorted(arr, key=lambda x:(-frequency[x], x))
        return sortedArray
