# User function Template for python3

class Solution:
    def palindromicPartition(self, string):
        # code here
        n = len(string)
        cuts = [0] * n

        # Function to check if a substring is a palindrome
        def isPalindrome(s, start, end):
            return s[start:end + 1] == s[start:end + 1][::-1]

        for i in range(n):
            minCuts = i

            for j in range(i, -1, -1):
                if isPalindrome(string, j, i):
                    if j == 0:
                        minCuts = 0
                    else:
                        minCuts = min(minCuts, 1 + cuts[j - 1])
            cuts[i] = minCuts
        return cuts[n - 1]
    