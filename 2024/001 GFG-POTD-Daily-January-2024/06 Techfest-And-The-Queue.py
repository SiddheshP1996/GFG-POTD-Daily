"""
Solution 1
"""

# User function Template for python3

from typing import List

class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        # Code here
        sumOfPowerInPrimeFactors = [i for i in range(b + 1)]
        count = 0

        for i in range(2, int(b ** 0.5) + 1):
            if sumOfPowerInPrimeFactors[i] == i:
                for j in range(i * i, b + 1, i):
                    if sumOfPowerInPrimeFactors[j] == j:
                        sumOfPowerInPrimeFactors[j] = i

        for num in range(a, b + 1):
            currentPrimeNumber = sumOfPowerInPrimeFactors[num]
            primeNumberCount = 0

            while num > 1:
                while num % currentPrimeNumber == 0:
                    num //= currentPrimeNumber
                    primeNumberCount += 1
                currentPrimeNumber = sumOfPowerInPrimeFactors[num]

            count += primeNumberCount

        return count

"""
Solution 2
"""
"""
# User function Template for python3

from typing import List

class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        # Code here
        sumOfPowerInPrimeFactors = [i for i in range(b + 1)]
        count = 0

        for i in range(2, int(b ** 0.5) + 1):
            if sumOfPowerInPrimeFactors[i] == i:
                for j in range(i * i, b + 1, i):
                    if sumOfPowerInPrimeFactors[j] == j:
                        sumOfPowerInPrimeFactors[j] = i

        for num in range(a, b + 1):
            currentNumber = num
            currentPrimeNumber = sumOfPowerInPrimeFactors[currentNumber]
            primeNumberCount = 0

            while currentNumber > 1:
                while currentNumber % currentPrimeNumber == 0:
                    currentNumber //= currentPrimeNumber
                    primeNumberCount += 1
                currentPrimeNumber = sumOfPowerInPrimeFactors[currentNumber]

            count += primeNumberCount

        return count
"""
