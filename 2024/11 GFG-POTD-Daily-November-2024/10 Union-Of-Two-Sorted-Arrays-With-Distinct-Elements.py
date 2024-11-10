# User function Template for python3

class Solution:
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):
        # Code here
        seen = set()
        for itemsInA in a:
            seen.add(itemsInA)
        for itemsInB in b:
            seen.add(itemsInB)
        return sorted(seen)
