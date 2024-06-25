# User function Template for python3

class Solution:
	def countPairs(self, mat1, mat2, n, x):
		# Code here
		setA = [j for i in mat1 for j in i]
		setB = [j for i in mat2 for j in i]
		setB = set(setB)
		result = 0
		for i in setA:
		    if x - i in setB:
		        result += 1
		return result
