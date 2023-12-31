# User function Template for python3

class Solution:
    def distinctSubsequences(self, S):
        # code here
        # Length of the input string
        n = len(S)

        # Initialize an array to store the number of distinct subsequences
        distinctSubsequencesCount = [0 if i > 0 else 1 for i in range(n + 1)]

        # Modulus value to prevent integer overflow
        mod = ((10 ** 9) + 7)

        # Dictionary to store the last occurrence index of each character
        lastOccurrence = {}

        # Loop through the characters of the input string
        for i in range(1, n + 1):
            character = S[i - 1]

            # Calculate the number of distinct subsequences for the current character
            distinctSubsequencesCount[i] = distinctSubsequencesCount[i - 1] * 2 % mod

            # Check if the current character has occurred before
            if character in lastOccurrence:
                index = lastOccurrence[character]
                # Subtract the count of subsequences ending with the previous occurrence
                distinctSubsequencesCount[i] -= distinctSubsequencesCount[index - 1] % mod

            # Update the last occurrence index of the current character
            lastOccurrence[character] = i

        # Return the final count of distinct subsequences modulo the specified value
        return distinctSubsequencesCount[n] % mod
