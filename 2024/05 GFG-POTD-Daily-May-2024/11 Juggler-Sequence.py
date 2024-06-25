# User function Template for python3

class Solution:
    def jugglerSequence(self, n):
        # Code here
        resultSequence = [n]
        
        while resultSequence[-1] != 1:
            temporaryStore = resultSequence[-1]
            if temporaryStore % 2 == 0:
                temporaryStore = temporaryStore ** (1 / 2)
            else:
                temporaryStore = temporaryStore ** (3 / 2)
            
            temporaryStore = int(temporaryStore)
            resultSequence.append(temporaryStore)
            
        return resultSequence
