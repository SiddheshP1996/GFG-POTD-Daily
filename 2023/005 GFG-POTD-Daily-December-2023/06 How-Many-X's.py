# Solution 1

# User function Template for python3

class Solution:
    def countX(self, L, R, X):
        # Code here
        count = 0
        i = L + 1
        while i < R:
            # find X in i and increment count
            count += str(i).count(str(X))
            i += 1
        return count


#  Solution 2

"""
class Solution:    
    def countX(self,L,R,X):
        #code here
        return sum([str(n).count(str(X)) for n in range(L+1,R)])
"""
