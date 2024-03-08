# User function Template for python3

class Solution:
    def sameFreq(self, s):
        # Code here
        frequency_dict = {}
        for char in s:
            frequency_dict[char] = frequency_dict.get(char, 0) + 1

        values = list(frequency_dict.values())
        distinct_values = set(values)

        if len(distinct_values) == 1:
            return True  # All characters already have the same frequency

        if len(distinct_values) > 2:
            return False  # More than 2 distinct frequencies cannot be balanced

        # If there are exactly 2 distinct frequencies, try removing one character
        if values.count(max(values)) == 1 and max(values) - min(values) == 1:
            return True
        elif values.count(min(values)) == 1 and min(values) == 1:
            return True
        return False
