# User function Template for python3

from typing import List

class Solution:
    def getPrimes(self, n : int) -> List[int]:
        # Code here
        # Helper function to generate prime numbers up to `n` using Sieve of Eratosthenes
        def sieve(n: int) -> List[bool]:
            isPrime = [True] * (n + 1)
            isPrime[0] = isPrime[1] = False
            primeNumber = 2
            while primeNumber * primeNumber <= n:
                if isPrime[primeNumber]:
                    for i in range(primeNumber * primeNumber, n + 1, primeNumber):
                        isPrime[i] = False
                primeNumber += 1
            return isPrime

        # Generate the list of primes up to `n`
        isPrime = sieve(n)

        # Find two primes that sum up to `n`
        for a in range(2, n // 2 + 1):
            b = n - a
            if isPrime[a] and isPrime[b]:
                return [a, b]
        
        return [-1, -1]
