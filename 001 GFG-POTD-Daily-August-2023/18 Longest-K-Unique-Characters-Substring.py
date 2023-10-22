# User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        if k <= 0 or k > 26:
            return -1

        char_count = {}
        longest_length = -1
        start = 0

        for end in range(len(s)):
            if s[end] not in char_count:
                char_count[s[end]] = 0
            char_count[s[end]] += 1

            while len(char_count) > k:
                char_count[s[start]] -= 1
                if char_count[s[start]] == 0:
                    del char_count[s[start]]
                start += 1

            if len(char_count) == k:
                longest_length = max(longest_length, end - start + 1)

        return longest_length
