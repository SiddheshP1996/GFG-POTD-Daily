# User function Template for python3

class Solution:
    def rowWithMax1s(self, arr):
        # Code here
        arrayLenght = len(arr[0])
        result = arrayLenght
        k =- 1
        for rowItem in range(len(arr)):
            for columnItem in range(arrayLenght):
                if arr[rowItem][columnItem] == 1:
                    if columnItem - 1 < result:
                        result = columnItem - 1
                        k = rowItem
                    if columnItem - 1 == -1:
                        return rowItem
                    break
        return k
