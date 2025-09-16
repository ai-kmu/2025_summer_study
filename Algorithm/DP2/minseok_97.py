class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)

        if len1 + len2 != len3:
            return False
        # dp[j]: s1의 i개 문자와 s2의 j개 문자로 s3의 i+j개 문자를 만들 수 있는지
        dp = [False] * (len2 + 1)

        for i in range(len1 + 1):
            for j in range(len2 + 1):       
                # 빈 string은 true         
                if i == 0 and j == 0:
                    dp[j] = True       
                # s1을 사용 안하면, 이전 상태가 참이고 s2의 현재 문자와 s3의 현재 문자가 같아야 함         
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1] 
                # s2를 사용 안하면, 이전 행의 같은 열 dp[j]가 참이고 s1의 현재 문자와 s3의 현재 문자가 같아야 함
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i - 1]
                # s1과 s2 모두 사용한다면
                else:
                    # s1의 이전 문자를 사용 했을 때 참이고, s1의 현재 문자와 s3의 현재 문자가 같을 때
                    match_from_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]
                    # s2의 이전 문자를 사용 했을 때 참이고, s2의 현재 문자와 s3의 현재 문자가 같을 때
                    match_from_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                    # 둘 중 하나라도 참이면 참임
                    dp[j] = match_from_s1 or match_from_s2
                
        return dp[len2]