# User function Template for python3

class Solution:
    def findLargest(self, N, S):
        # code here
        if N != 1 and S == 0:
            return -1
        elif N == 1 and S == 0:
            return 0
        else:
            result = ""
            while len(result) != N:
                if S > 9:
                    result += str(9)
                    S -= 9
                else:
                    result += str(S)
                    S = 0
            if S == 0:
                return result
            else:
                return -1
