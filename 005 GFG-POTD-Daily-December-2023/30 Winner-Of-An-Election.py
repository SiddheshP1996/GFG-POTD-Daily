# User function Template for python3

from collections import Counter

class Solution:
    
    # Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self, arr, n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        return sorted(Counter(arr).items(), key = lambda x:(-x[1], x[0]))[0]
