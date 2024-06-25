# User function Template for python3

class Solution:
    
    # Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        # Your code here
        tempDict = {}
        result, count = [], 0
        for i in arr:
            if count == 2:
                break
            tempDict[i] = tempDict.get(i, 0) + 1
            if tempDict[i] == 2:
                result.append(i)
                count += 1
        return result
