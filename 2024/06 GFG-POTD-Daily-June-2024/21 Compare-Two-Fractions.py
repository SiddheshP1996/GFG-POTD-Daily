# User function Template for python3

class Solution:
    def compareFrac (self, str):
        # Code here
        stringList = str.split(",")
        
        if stringList[0] == stringList[1]:
            return "equal"
            
        first = stringList[0].split("/")
        last = stringList[1].split("/")
        
        resultFirst = int(first[0]) / int(first[1])
        resultLast = int(last[0]) / int(last[1])
        
        if resultFirst == resultLast:
            return "equal"
        
        if resultFirst > resultLast:
            return stringList[0].strip()
            
        return stringList[1].strip()
