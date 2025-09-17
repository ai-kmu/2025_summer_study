from typing import List

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False  # 길이가 다르면 불가능
        
        # dp[i][j] = s1의 i글자, s2의 j글자를 사용해서 s3의 i+j 글자 만들 수 있는지
        dp = [[False]*(n+1) for _ in range(m+1)]
        
        dp[0][0] = True  # 아무것도 사용하지 않으면 True
        
        # 첫 번째 행 (s1은 0글자, s2만 사용)
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        # 첫 번째 열 (s2는 0글자, s1만 사용)
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        # 나머지 dp 채우기
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 두 가지 경우 중 하나라도 가능하면 True
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) \
                           or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[m][n]
