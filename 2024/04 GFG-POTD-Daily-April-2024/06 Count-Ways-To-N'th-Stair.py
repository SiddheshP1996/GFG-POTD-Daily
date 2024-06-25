# User function Template for python3

class Solution:
    """
    Function to count number of ways to reach the nth stair
    when order does not matter.
    """
    def countWays(self, n):
        mod = 1000000007
        # Code here
        return(n - (n // 2) - (n % 2) + 1)
