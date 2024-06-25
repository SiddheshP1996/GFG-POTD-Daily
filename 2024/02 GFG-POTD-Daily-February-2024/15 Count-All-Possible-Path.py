# User function Template for python3

class Solution:
	def isPossible(self, paths):
		# Code here
		for path in paths:
		    if path.count(1) % 2:
		        return 0
		return 1
