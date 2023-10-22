# User function Template for python3

class Solution:
    def rotate(self, N, D):
        # code here
        D = D % 16
        N = format(N, '016b')
        return[int(N[D:] + N[:D], 2), int(N[-D:] + N[:-D], 2)]