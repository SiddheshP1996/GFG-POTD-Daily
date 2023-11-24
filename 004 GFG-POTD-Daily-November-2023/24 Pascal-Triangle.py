# User function Template for python3

class Solution:

    def nthRowOfPascalTriangle(self,n):
        # code here
        mod = ((10**9) + 7)
        results = [[] for i in range (n+1)]
        #results[1] = [1]
        if n == 1 : return [1]
        results[2] = [1,1]
        for i in range(3, n+1):
            results[i].append(1)
            prev = results[i-1]
            leftOne = 0
            rightOne = 1
            while(rightOne < (i - 1)):
                results [i] .append((prev[leftOne] + prev[rightOne]) % mod)
                leftOne += 1
                rightOne += 1
            results[i].append(1)
        return results[n]
