# User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        # Code here
        n = len(S)
        countOf0 = countOf1 = countOf2 = 0
        
        startWindow = endWindow = 0
        
        windowMinLength = float('inf')
        
        while endWindow < n:
            if S[endWindow] == '0':
                countOf0 += 1
            elif S[endWindow] == '1':
                countOf1 += 1
            elif S[endWindow] == '2':
                countOf2 += 1
            
            while countOf0 > 0 and countOf1 > 0 and countOf2 > 0:
                windowMinLength = min(windowMinLength, endWindow - startWindow + 1)
                
                if S[startWindow] == '0':
                    countOf0 -= 1
                elif S[startWindow] == '1':
                    countOf1 -= 1
                elif S[startWindow] == '2':
                    countOf2 -= 1
                
                startWindow += 1
            
            endWindow += 1
        
        return windowMinLength if windowMinLength != float('inf') else -1
