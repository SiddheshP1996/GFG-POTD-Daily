# User function Template for python3

class Solution:
	def maxDotProduct(self, n, m, a, b):
		# Code here
		dp = [[0] * (m + 1) for item in range(n + 1)]
		
		for i in range(n + 1):
		    dp[i][0] = 0
		    
		for j in range(1, m + 1):
		    dp[0][j] = float('-inf')
		    
		for i in range(1, n + 1):
		    for j in range(1, m + 1):
		        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + a[i - 1] * b[j - 1])
		        
		return dp[n][m]
