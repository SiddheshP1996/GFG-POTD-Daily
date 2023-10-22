# User function Template for python3

# Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self, arr, n, s):
        # Write your code here
        l = 0
        r = 0
        flag = False
        summation = arr[0]

        if s == 0:
            return [-1]
        while r < n:
            if summation == s:
                flag = True
                break
            elif summation < s:
                r += 1
                if r < n:
                    summation += arr[r]
            else:
                summation -= arr[l]
                l += 1
        if flag:
            return l + 1, r + 1
        return [-1]