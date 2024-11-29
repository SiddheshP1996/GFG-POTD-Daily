# User function Template for python3

class Solution:
	def addBinary(self, s1, s2):
		# Code here
		stringOne = int(s1, 2)
		stringTwo = int(s2, 2)
		
		return bin(stringOne + stringTwo)[2:]
