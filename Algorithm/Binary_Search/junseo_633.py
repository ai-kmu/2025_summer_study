import math

class Solution(object):
    def judgeSquareSum(self, c):
        for a in range(0,math.isqrt(c)+1): # a^2 <= c이므로 a는 0부터 sqrt(c)까지 탐색
            b = c - a**2
            if math.isqrt(b)**2 == b: # sqrt(b)의 정수 제곱이 b와 같은지
                return True
        return False
        