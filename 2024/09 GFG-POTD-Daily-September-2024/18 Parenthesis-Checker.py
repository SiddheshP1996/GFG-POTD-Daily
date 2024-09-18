# User function Template for python3

class Solution:
    
    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        # Code here
        bracketStack = []
        bracketMap = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        
        for character in x:
            if character in bracketMap:
                bracketStack.append(character)
            else:
                if not bracketStack or\
                    bracketMap[bracketStack.pop()] != character:
                        return False
        return not bracketStack
