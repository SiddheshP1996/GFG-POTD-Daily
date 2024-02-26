# User function Template for python3

class Solution:
    def AllPossibleStrings(self, s):
        # Code here
        result = []
        
        def execute(strings, item):
            if item == len(s):
                return
        
            result.append(strings + s[item])
            
            execute(strings + s[item], item + 1)
            execute(strings, item + 1)
        execute("", 0)
        return sorted(result)
