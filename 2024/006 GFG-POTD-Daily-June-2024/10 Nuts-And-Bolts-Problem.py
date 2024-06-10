# User function Template for python3

class Solution:
    def matchPairs(self, n, nuts, bolts):
        # Code here
        order = {'!':1,'#':2,'$':3,'%':4,'&':5,'*':6,'?':7,'@':8,'^':9}
        mapNuts = [order[i] for i in nuts]
        mapBolts = [order[j] for j in bolts]
        mapNuts.sort()
        mapBolts.sort()
        reverseOrder = {v:k for k,v in order.items()}
        nuts[:] = [reverseOrder[i] for i in mapNuts]
        bolts[:] = [reverseOrder[j] for j in mapBolts]
