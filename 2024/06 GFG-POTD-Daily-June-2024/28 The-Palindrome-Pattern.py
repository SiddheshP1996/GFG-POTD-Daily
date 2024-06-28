# User function Template for python3

class Solution:
    def isPalindrome(self, stringOfNums):
        return stringOfNums == stringOfNums[::-1]
    
    def pattern (self, arr):
        # Code here
        for rows in range(len(arr)):
            if self.isPalindrome(arr[rows]):
                return str(rows) + " R"

        for rows in range(len(arr)):
            columns = [arr[j][rows] for j in range(len(arr))]
            if self.isPalindrome(columns):
                return str(rows) + " C"
        return -1
