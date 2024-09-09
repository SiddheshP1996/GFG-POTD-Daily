# User function Template for python3

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # Code here
        resultList = list()
        onesCount = 0
        twosCount = 0

        for i in range(len(arr)):
            if arr[i] == 0:
                resultList.append(0)
            elif arr[i] == 1:
                onesCount += 1
            else:
                twosCount += 1
                
        for ones in range(onesCount):
            resultList.append(1)
            
        for twos in range(twosCount):
            resultList.append(2)
            
        for i in range(len(arr)):
            arr[i] = resultList[i]
