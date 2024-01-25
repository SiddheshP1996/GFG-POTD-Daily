# User function Template for python3

class Solution:
    def solve(self, num1, num2):
        # Code here
        def isPrime(n):
            if n == 2 or n == 3:
                return True
            if n <= 1 or n % 2 == 0 or n % 3 == 0:
                return False
            prime_check = int((n ** 0.5) + 1)
            for i in range(5, prime_check, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True
            
        if num1 == num2:
            return 0
        primeNum = [False] * 10000
        for i in range(1000, 10000):
            primeNum[i] = isPrime(i)
            
        queueBFS = [(num1, 0)]
        not_visited = [True] * 10000
        while queueBFS:
            current_state = queueBFS[0]
            queueBFS.pop(0)
            for i in range(1, 10):
                for j in [1, 10, 100, 1000]:
                    num = current_state[0] + i * j
                    if current_state[0] % (j * 10) > num % (j * 10):
                        num -= j * 10
                    if primeNum[num]:
                        if num == num2:
                            return current_state[1] + 1
                        elif not_visited[num]:
                            not_visited[num] = False
                            queueBFS.append((num, current_state[1] + 1))
        return -1
