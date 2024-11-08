# User function Template for python3

class Solution:
    def minRepeats(self, s1, s2):
        # Code here
        stringS1 = set(s1)
        stringS2 = set(s2)
        
        for k in stringS2:
            if k not in stringS1:
                return -1
                
        count = 1
        c = len(s2)
        new_s1 = s1
        
        # rounds
        while len(new_s1) <= 2*c:
            if new_s1.find(s2) != -1:
                return count
            count += 1
            new_s1 += s1
            
        # one extra round
        if new_s1.find(s2) != -1:
                return count
            
        return -1
