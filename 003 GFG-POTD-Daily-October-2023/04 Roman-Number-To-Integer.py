# User function Template for python3

class Solution:
    def romanToDecimal(self, S):
        # code here
        result = 0

        romanNumbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for i in range(len(S)):
            c = S[i]
            n = ""
            if i + 1 < len(S):
                n = S[i + 1]
            if c == 'I':
                if n == 'V' or n == 'X':
                    result += -romanNumbers[c]
                    continue
            if c == 'X':
                if n == 'L' or n == 'M' or n == 'C':
                    result += -romanNumbers[c]
                    continue
            if c == 'C':
                if n == 'D' or n == 'M':
                    result += -romanNumbers[c]
                    continue
            result += romanNumbers[c]
        return result
