# User function Template for python3


# Function to find the maximum possible amount of money we can win.
class Solution:
    def optimalStrategyOfGame(self, n, arr):
        # Code here
        memory = {}
        def dfs(left, right):
            if(left, right) in memory:
                return memory[(left, right)]
            if left > right:
                return 0
            positionOne = arr[left] + min(dfs(left + 1, right - 1), dfs(left + 2, right))
            positionTwo = arr[right] + min(dfs(left, right - 2), dfs(left + 1, right - 1))
            
            maximum = max(positionOne, positionTwo)
            memory[(left, right)] = maximum
            return memory[(left, right)]
        return dfs(0, n - 1)
