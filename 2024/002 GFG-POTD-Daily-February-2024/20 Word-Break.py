# User function Template for python3

class Solution:
    def wordBreak(self, n, s, dictionary):
        # Complete this function
        def execute(s):
            if not s:
                return True
            for item in dictionary:
                if s.startswith(item) and execute(s[len(item):]):
                    return True
            return False
        return execute(s)
