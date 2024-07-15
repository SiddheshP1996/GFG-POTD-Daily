# User function Template for python3
class Solution:
    def smallestNumber(self, s, d):
        # Code here
        result = ""
        remainder = s

        for i in range(1, d + 1):
            if i == 1:
                remainingSum = (d - 1) * 9
                if remainingSum + 9 < s:
                    return "-1"
                digit = max(1, s - remainingSum)
                s -= digit
                result += str(digit)
                continue
            
            digit = s - (d - i) * 9
            if digit <= 0:
                result += "0"
            else:
                result += str(digit)
                s -= digit

        return result
