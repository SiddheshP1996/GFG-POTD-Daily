# User function Template for python3

class Solution:
	def isEularCircuitExist(self, v, adj):
		# Code here
		return all([len(a) % 2 == 0 for a in adj])
