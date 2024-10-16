# User function Template for python3

class Solution:
    def findAndPlace(self, arr, idx):
        value = idx + 1
        targetIndex = arr.index(value)
        arr[idx], arr[targetIndex] = arr[targetIndex], arr[idx]
        
    def checkSorted(self, arr):
        # Code here
        misplaced = 0
        for index, value in enumerate(arr):
            if value != index + 1:
                misplaced += 1
                self.findAndPlace(arr, index)
            if misplaced > 2:
                return False
        
        if misplaced in (0, 2):
            return True
        return False
