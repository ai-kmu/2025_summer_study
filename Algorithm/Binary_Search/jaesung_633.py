#633
class Solution(object):
    def judgeSquareSum(self, c):
        left = 0
        right = int(c ** 0.5)
        while left <= right:
            result = left*left + right*right
            if result == c:
                return True
            elif result < c:
                left += 1
            elif result > c:
                right -= 1
        return False
