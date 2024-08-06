# User function Template for python3

class Solution:
    def isValid(self, str):
        # Code here
        addressIPString = str.split(".")
        if len(addressIPString) != 4:
            return False
        
        for i in addressIPString:
            if(i != ""):
                if(int(i) < 0 or \
                    (i[0] == "0" and len(i) > 1) or \
                        int(i) > 255):
                    return False
            else:
                return False
            
        return True
