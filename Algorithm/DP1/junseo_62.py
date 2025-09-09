import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # (m+n-2)번 중에서 (m-1)번 아래로 가는 경우의 수
        return math.comb(m + n - 2, m - 1)