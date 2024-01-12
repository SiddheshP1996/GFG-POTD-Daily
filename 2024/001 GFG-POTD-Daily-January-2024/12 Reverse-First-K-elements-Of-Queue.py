# User function Template for python3

"""
Function Arguments :
		@param  : q ( given queue to be used), k(Integer )
		@return : list, just reverse the first k elements of queue and return new queue
"""

# Function to reverse first k elements of a queue.

class Solution:
    def modifyQueue(self, q, k):
        # Code here
        i = 0
        j = k - 1
        while i < j:
            q[i], q[j] = q[j], q[i]
            i += 1
            j -= 1
        return q
