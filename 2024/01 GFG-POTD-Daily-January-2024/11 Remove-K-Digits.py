# User function Template for python3

class Solution:

    def removeKdigits(self, S, K):
        # Code here
        digitStack = []
        for i in S:
            while digitStack and K > 0 and i < digitStack[-1]:
                K -= 1
                digitStack.pop()
            digitStack.append(i)
        while K > 0:
            digitStack.pop()
            K -= 1
        if len(digitStack) == digitStack.count('0'):
            return '0'
        for i in range(len(digitStack)):
            if digitStack[i] == '0':
                continue
            if digitStack[i] != '0':
                return "".join(digitStack[i:])
