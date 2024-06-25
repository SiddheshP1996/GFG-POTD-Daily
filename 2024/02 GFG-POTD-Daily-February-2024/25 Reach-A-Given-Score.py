# User function Template for python3

class Solution:
    def count(self, n: int) -> int:
        # Your code here
        arr = [0] * (n + 1)
        arr[0] = 1
        for i in range(3, n + 1):
            arr[i] += arr[i - 3]
        for i in range(5, n + 1):
            arr[i] += arr[i - 5]
        for i in range(10, n + 1):
            arr[i] += arr[i - 10]
        return arr[-1]
