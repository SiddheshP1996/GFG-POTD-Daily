# User function Template for python3

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        # Your Code goes here.
        if not nums:
            return [-1]
        
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        result = []
        for candidate in [candidate1, candidate2]:
            if nums.count(candidate) > len(nums) // 3:
                result.append(candidate)
        
        return result if result else [-1]
