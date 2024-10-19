# User function Template for python3

import sys

class Solution:
    def roundToNearest (self, s) : 
        # Complete the function
        sys.set_int_max_str_digits(10 ** 5)
        x = int(s)
        temp = x // 10
        remainder = x % 10
        leadZero = len(s) - len(str(x))
        
        if remainder > 5:
            result = (temp * 10) + 10
        else:
            result = temp * 10
            
        result = '0' * leadZero + str(result)
        return result
