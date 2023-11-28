# User function Template for python3

class Solution:
    def sumOfDependencies(self,adj,V):
        # code here
        summation = 0
        for i in adj:
            summation = summation + len(i)
        return summation
