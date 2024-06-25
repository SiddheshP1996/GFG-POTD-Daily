# User function Template for python3

class Solution:
    def ExtractNumber(self, sentence):
        # Code here
        for item in sorted(sentence.split(), key = lambda x: (len(x), x), reverse=True):
            if item.isnumeric() and '9' not in item:
                return item
        return -1
