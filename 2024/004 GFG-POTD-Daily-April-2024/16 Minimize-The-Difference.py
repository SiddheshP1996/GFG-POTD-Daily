# User function Template for python3

from typing import List

class Solution:
    def minimizeDifference(self, n : int, k : int, arr : List[int]) -> int:
        # Code here
        prefixPart, suffixPart = [], []
        minumum, maximum = arr[0], arr[0]
        for i in range(n - k):
            minumum = min(minumum, arr[i])
            maximum = max(maximum, arr[i])
            prefixPart.append([minumum, maximum])
        
        minumum, maximum = arr[-1], arr[-1]
        for i in range(n - 1, k - 1, -1):
            minumum = min(minumum, arr[i])
            maximum = max(maximum, arr[i])
            suffixPart.append([minumum, maximum])
        suffixPart = suffixPart[::-1]
        i, j= -1, 0
        result = float("inf")
        while(j <= n - k):
            if(i == -1):
                difference = suffixPart[j][1] - suffixPart[j][0]
                result = min(result, difference)
            elif(j == n - k):
                difference = prefixPart[i][1] - prefixPart[i][0]
                result = min(result, difference)
            else:
                prefix, suffix = prefixPart[i] , suffixPart[j]
                difference = max(prefix[1], suffix[1]) - min(prefix[0], suffix[0])
                result = min(result, difference)
            i += 1
            j += 1
        return(result)