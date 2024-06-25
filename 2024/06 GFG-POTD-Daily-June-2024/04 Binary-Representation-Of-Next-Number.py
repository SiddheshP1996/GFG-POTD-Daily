# User function Template for python3

class Solution:
	def binaryNextNumber(self, s):
		# Code here
		return bin(int(s, 2) + 1)[2:]
