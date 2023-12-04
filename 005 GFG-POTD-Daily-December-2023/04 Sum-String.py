# User function Template for python3
class Solution:
    def isSumString(ob, S):
        # code here
        # write a function to check the string
        def check(stringOfDigit1, stringOfDigit2, stringOfDigit):
            # Base case: if stringOfDigit is empty, the current substrings form a valid sum string
            if stringOfDigit == "":
                return True
            # Base case: if stringOfDigit is empty, the current substrings form a valid sum string
            stringOfDigit3 = str(int(stringOfDigit1) + int(stringOfDigit2))

            n = len(stringOfDigit3)
            # Base case: if stringOfDigit is empty, the current substrings form a valid sum string
            if stringOfDigit[:n] == stringOfDigit3:
                # Recursively check the remaining part of stringOfDigit with updated substrings
                return check(stringOfDigit2, stringOfDigit3, stringOfDigit[n:])
            # If the match fails, the substrings do not form a valid sum string
            return False

        n = len(S)
        # Iterate through possible split points for the first two substrings
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                # Extract the first two substrings
                stringOfDigit1, stringOfDigit2 = S[:i], S[i:j]
                # Check if the remaining part of the string is a valid sum string
                if check(stringOfDigit1, stringOfDigit2, S[j:]):
                    # is a valid substring
                    return 1
        # no valid substring has been found
        return 0
    