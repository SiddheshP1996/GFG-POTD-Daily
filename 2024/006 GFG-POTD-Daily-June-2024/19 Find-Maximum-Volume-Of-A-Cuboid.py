# User function Template for python3

from math import sqrt, pow

class Solution:
    def maxVolume(self, perimeter, area):
        # Code here
        length = (perimeter - sqrt(pow(perimeter, 2) - 24 * area)) / 12
        height = (perimeter / 4) - (2 * length)
        volume = pow(length, 2) * height
        return volume
