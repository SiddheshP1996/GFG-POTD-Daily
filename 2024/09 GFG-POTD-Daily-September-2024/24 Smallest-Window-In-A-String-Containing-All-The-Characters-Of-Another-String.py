# User function Template for python3

from collections import Counter

class Solution:
    
    # Function to find the smallest window in the string s consisting
    # of all the characters of string p.
    def smallestWindow(self, s, p):
        # Code here
        pCount = Counter(p)
        required = len(pCount)
        left, right = 0, 0
        formed = 0
        windowCounts = {}
        
        minLength = float('inf')
        minLeft = 0
        
        while right < len(s):
            character = s[right]
            windowCounts[character] = windowCounts.get(character, 0) + 1
            
            if character in pCount and windowCounts[character] == pCount[character]:
                formed += 1
            while left <= right and formed == required:
                character = s[left]
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    minLeft = left
                    
                windowCounts[character] -= 1
                if character in pCount and windowCounts[character] < pCount[character]:
                    formed -= 1
                
                left += 1
            right += 1

        return s[minLeft:minLeft + minLength] if minLength != float('inf') else "-1"
