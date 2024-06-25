# User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self, inputString):
        # code here
        # Get the length of the input string
        stringLength = len(inputString)

        # Initialize a 2D array for dynamic programming
        dp = [[0] * stringLength for _ in range(stringLength)]

        # Initialize the base cases for substrings of length 1 (single characters)
        for i in range(stringLength):
            dp[i][i] = 1

        # Fill the DP table for substrings of length 2 and above
        for substringLength in range(2, stringLength + 1):
            for startIndex in range(stringLength - substringLength + 1):
                endIndex = startIndex + substringLength - 1

                # Check if the characters at both ends of the substring match
                if inputString[startIndex] == inputString[endIndex] and substringLength == 2:
                    # Special case: Substring of length 2 with matching characters
                    dp[startIndex][endIndex] = 2
                elif inputString[startIndex] == inputString[endIndex]:
                    # Characters match, so update the DP table using the result from a shorter substring
                    dp[startIndex][endIndex] = dp[startIndex + 1][endIndex - 1] + 2
                else:
                    # Characters don't match, so take the maximum from two possible options
                    dp[startIndex][endIndex] = max(dp[startIndex][endIndex - 1], dp[startIndex + 1][endIndex])

        # The minimum number of deletions required to form a palindrome is the complement of the longest palindromic
        # subsequence
        return stringLength - dp[0][stringLength - 1]
