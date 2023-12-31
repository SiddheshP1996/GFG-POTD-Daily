# User function Template for python3

class Solution:
    def shuffleArray(self, arr, n):
        # Your code goes here
        middleElement = n // 2

        for i in range(middleElement):
            arr.insert(((2 * i) + 1), arr[middleElement + i])
            arr.pop(middleElement + i + 1)
        return arr
