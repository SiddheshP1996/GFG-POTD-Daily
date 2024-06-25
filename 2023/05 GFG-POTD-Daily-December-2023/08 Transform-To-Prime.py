# User function Template for python3

class Solution:
    def minNumber(self, arr, n):
        # Code here
        def numberIsPrime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        def nextPrimeNumber(num):
            while True:
                if numberIsPrime(num):
                    return num
                num += 1

        sumOfNumberInArray = sum(arr)
        nextPrimeNumber = nextPrimeNumber(sumOfNumberInArray)
        return nextPrimeNumber - sumOfNumberInArray
