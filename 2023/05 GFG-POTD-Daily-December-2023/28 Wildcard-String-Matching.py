# User function Template for python3

import re

class Solution:
    def match(self, wild, pattern):
        # Code here
        # Convert the wild pattern to a regular expression pattern
        regexPattern = '^' + wild.replace('?', '.').replace('*', '.*') + '$'

        # Use re.fullmatch to check if the entire text matches the regular expression pattern
        return True if re.fullmatch(regexPattern, pattern) else False
