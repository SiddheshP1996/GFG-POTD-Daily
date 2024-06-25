# User function Template for python3

from bisect import bisect_right

class Solution:
	def min_operations(self, nums):
		# Code here
		n = len(nums)
		numList = [nums[0]]
		for element in range(1, n):
		    num = nums[element] - element
		    position = bisect_right(numList, num)
		    if position == len(numList):
		        numList.append(num)
		    else:
		        numList[position] = num
		        
		return n - len(numList)
