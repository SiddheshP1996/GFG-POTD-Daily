# User function Template for python3

class Solution:
    def search(self, pat, txt):
        # Code here
        patSize = len(pat)
        textSize = len(txt)
        listOne = []
        
        for i in range(0, patSize - 1 + textSize):
            s = txt[i:i + patSize]
            if s == pat:
                listOne.append(i)
        
        return listOne
