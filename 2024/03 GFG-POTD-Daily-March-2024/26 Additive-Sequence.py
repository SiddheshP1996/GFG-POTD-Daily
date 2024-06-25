# User function Template for python3

# return 1 in case of True and 0 in case of False

def getSequence(string_a, string_b, n):
    length = len(string_a) + len(string_b)
    num_string_array = [string_a, string_b]
    i = 2
    while True:
        addition = int(num_string_array[i - 1]) + int(num_string_array[i - 2])
        num_string_array.append(str(addition))
        length += len(num_string_array[-1])
        i += 1
        if length >= n:
            break
    if len(num_string_array) == 2:
        return ''
    return ''.join(num_string_array)

def execute(num_string):
    n = len(num_string)
    for i in range(n):
        string_a = num_string[:i + 1]
        for j in range(i + 1, n):
            string_b = num_string[i + 1: j + 1]
            x = getSequence(string_a, string_b, n)
            if num_string == x:
                return 1
    return 0

class Solution:
    def isAdditiveSequence(self, n):
        # Code here
        return execute(n)
