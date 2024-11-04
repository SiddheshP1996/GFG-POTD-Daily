# User function Template for python3
class Solution:
    def findTriplets(self, arr):
        # Your code here
        result = []
        arrDict = dict()
        
        for index, item in enumerate(arr):
            arrDict[item] = arrDict.get(item, [])
            arrDict[item].append(index)
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                arrSum = arr[i] + arr[j]
                
                for k in arrDict.get(-arrSum, []):
                    if k > i and k > j:
                        result.append(sorted([i, j, k]))
        
        return result
