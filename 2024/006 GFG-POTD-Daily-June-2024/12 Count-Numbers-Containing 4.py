# User function Template for python3

class Solution:
    def countNumberswith4(self, n : int) -> int:
        # Code here
        number4Count = 0
        for i in range(n+1):
            if "4" in str(i):
                number4Count += 1
        return number4Count
