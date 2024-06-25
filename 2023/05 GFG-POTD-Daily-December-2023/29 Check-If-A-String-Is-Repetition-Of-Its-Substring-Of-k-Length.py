from collections import Counter

class Solution:
    def kSubstrConcat(self, n, s, k):
        # Your Code Here
        if n % k != 0:
            return 0
        
        listOfString = []
        
        for i in range(0, n, k):
            elementOfSubString = s[i]
        
            for j in range(1, k):
                elementOfSubString += s[i + j]
            listOfString.append(elementOfSubString)
        
        dictionaryCount = Counter(listOfString)
        
        if len(dictionaryCount) > 2:
            return 0

        updateCount = 0
        
        for i in dictionaryCount:
            if dictionaryCount[i] > 1:
                updateCount += 1

        if updateCount == 2:
            return 0
        
        return 1
