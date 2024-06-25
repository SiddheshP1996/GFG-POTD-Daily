# User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here
        digits = [int(i) for i in str(n)]
        result = sum(i ** 3 for i in digits)
        return "true" if result == n else "false"
