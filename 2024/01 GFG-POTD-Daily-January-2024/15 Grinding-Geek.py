# User function Template for python3

from typing import List


class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        # Code here
        dp = [0 for allCourses in range(total + 1)]
        for courses in reversed(cost):
            for totalPrice in range(total, courses - 1, -1):
                dp[totalPrice] = max(dp[totalPrice], dp[totalPrice - (courses + 9)//10] + 1)
        return dp[total]
