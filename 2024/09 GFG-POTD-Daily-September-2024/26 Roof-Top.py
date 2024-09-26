# User function Template for python3
 
class Solution:
    
    # Function to find maximum number of consecutive steps 
    # to gain an increase in altitude with each step.
    def maxStep(self, arr):
        # Your code here
        currentStep = 0
        maxSteps = 0
        
        # Iterate through the buildings from the second one
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                currentStep +=1
                maxSteps = max(maxSteps, currentStep)
            else:
                currentStep = 0
                
        return maxSteps
