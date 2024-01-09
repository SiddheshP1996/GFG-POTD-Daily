# User function Template for python3

class Solution:
    def search(self, pat, txt):
        # Code here
        newText = len(txt)
        newPatttern = len(pat)
        
        result = []
        
        for i in range(newText - newPatttern + 1):
            if txt[i:i + newPatttern] == pat:
                result.append(i + 1)
        if result == []:
            return [-1]
        else:
            return result
