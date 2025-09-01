# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         down = m-1
#         right = n-1
#         total = down+right
#         comb = min(down,right)
#         result = 1
#         for i in range(comb):
#             result *= (total - i)
#             result //= (i + 1)
#         return result

class Solution:
    def uniquePaths(self, m: int, n: int):
        dp = [[0]*n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 or j == n-1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]
