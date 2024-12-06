# User function Template for python3

class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        # Code here
        arr.sort(reverse = True)
        return sum(1 for i, x in enumerate(arr) if x > i)
