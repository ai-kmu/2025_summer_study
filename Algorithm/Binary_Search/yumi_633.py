import math

class Solution(object):
    def judgeSquareSum(self, c):
        
        max_val = int(math.isqrt(c))
        for a in range(-max_val, max_val+1):
            b_squared = c - a**2
            if b_squared < 0:
                continue
            b = int(math.isqrt(b_squared))
            if b**2 == b_squared:
                return True

        return False
        
