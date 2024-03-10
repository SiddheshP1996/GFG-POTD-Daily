# User function Template for python3

class Solution:
    def removeDuplicates(self, str):
        # Code here
        l = []
        for i in str:
            if i not in l:
                l.append(i)
        return "".join(l)
