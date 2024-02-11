# User function Template for python3

class Solution:
    def recamanSequence(self, n):
        # Code here
        sequence = [0]
        sequenceNumberAppeared = set()
        
        for i in range(1, n):
            previousTerm = sequence[-1]
            nextTerm = previousTerm - i
            
            if nextTerm > 0 and nextTerm not in sequenceNumberAppeared:
                sequence.append(nextTerm)
                sequenceNumberAppeared.add(nextTerm)
            else:
                nextTerm = previousTerm + i
                sequence.append(nextTerm)
                sequenceNumberAppeared.add(nextTerm)
                
        return sequence
