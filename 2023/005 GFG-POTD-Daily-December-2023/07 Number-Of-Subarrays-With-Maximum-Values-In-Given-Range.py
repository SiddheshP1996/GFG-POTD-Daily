# User function Template for python3

class Solution:
    def countSubarrays(self, a,n,L,R):
        # Complete the function
        listOfArray=[i for i in range(n) if a[i] > R]
        result, j, c = [0] * 3
        for i in range(n):
            if j == len(listOfArray) or i < listOfArray[j]:
                if a[i] >= L:
                    if j == len(listOfArray):
                        result += (c + 1) * (n - i)
                    else:
                        result += (c + 1) * (listOfArray[j] - i)
                    c = 0
                else:
                    c += 1
            else:
                c = 0
                j += 1
        return result
