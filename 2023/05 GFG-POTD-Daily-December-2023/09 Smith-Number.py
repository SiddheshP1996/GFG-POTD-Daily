# User function Template for python3

def sumOfDigits(n):
    # Find sum of digit
    sumOfDigits = 0
    while n > 0 :
        sumOfDigits += n % 10
        n //= 10
    return sumOfDigits


def sumIsPrime(n):
    sumIsPrime = 0
    while n!=1 :
        i = 2
        while n % i != 0 :
            i += 1
        n //= i
        sumIsPrime += sumOfDigits(i)
    return sumIsPrime


def numberIsPrime(n):
    if n <= 1 :
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 :
            return 0
    return 1


class Solution:
    def smithNum(self, n):
        # Code here
        return 1 if (sumOfDigits(n) == sumIsPrime(n) and numberIsPrime(n) == 0 ) else 0
