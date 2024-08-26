# Your task is to complete this function
# Function should return True/False or 1/0
# str1: pattern
# str2: text

import re

class Solution:
    def wildCard(self, pattern, string):
        # Code here
        p = "^" + re.sub("\*+", "[a-z]*", pattern).replace("?", "[a-z]") + "$"
        return 1 if re.search(p, string) else 0
