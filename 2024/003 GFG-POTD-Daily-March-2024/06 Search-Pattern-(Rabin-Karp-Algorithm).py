# User function Template for python3

class Solution:
    def search(self, pattern, text):
        # Code here
        patternLength = len(pattern)
        textLength = len(text)
        indexes = []
        
        for i in range(textLength - patternLength + 1):
            if text[i: i + patternLength] == pattern:
                indexes.append(i + 1)
        return indexes
