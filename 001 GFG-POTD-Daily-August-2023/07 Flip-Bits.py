#User function Template for python3

class Solution:
    def maxOnes(self, a, n):
        # Your code goes here
        net_gain=0
        current_sum=0
        count_ones=0
        for i in range(len(a)):
            if a[i]==0:
                current_sum+=1
                net_gain=max(net_gain,current_sum)
            elif a[i]==1:
                if current_sum-1>0:
                    current_sum-=1
                else:
                    current_sum=0
                count_ones+=1
        return count_ones+net_gain