class Solution(object):
    def uniquePaths(self, m, n):

        # 1. dp 테이블 생성 (m x n)
        dp = [[0] * n for _ in range(m)]
        
        # 2. 첫 행과 첫 열 초기화
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
            
        # 3. 점화식 적용
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # 4. 결과 반환
        return dp[m-1][n-1]

        
