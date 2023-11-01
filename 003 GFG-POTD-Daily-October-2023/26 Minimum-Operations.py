# User function Template for python3

class Solution:
    def minOperation(self, n):
        # code here
        def count(number):
            if number == 0:
                return 0
            if number % 2 == 0:
                return 1 + count(number // 2)
            return 1 + count(number - 1)

        return count(n)
