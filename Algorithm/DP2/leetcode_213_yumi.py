from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]  # 집이 하나면 그 집만 털 수 있음
        
        # 일반적인 DP 로직: 직선 형태로 rob
        def rob_linear(houses: List[int]) -> int:
            m = len(houses)
            # dp[i][0] = i번째 집을 털지 않았을 때 최대 금액
            # dp[i][1] = i번째 집을 털었을 때 최대 금액
            dp = [[0, 0] for _ in range(m)]
            
            # 첫 집 초기화
            dp[0][0] = 0       # 안 털면 0
            dp[0][1] = houses[0]  # 털면 houses[0]
            
            for i in range(1, m):
                # i번째 집 안 털 경우: 이전 집을 털었든 안 털었든 상관 없음
                dp[i][0] = max(dp[i-1][0], dp[i-1][1])
                
                # i번째 집 털 경우: 이전 집은 반드시 안 털어야 함
                dp[i][1] = dp[i-1][0] + houses[i]
            
            # 마지막 집까지 고려한 최대값
            return max(dp[m-1][0], dp[m-1][1])
        
        # 원형 때문에 경우 나누기
        # 1) 첫 집 포함, 마지막 집 제외
        money1 = rob_linear(nums[:-1])
        # 2) 첫 집 제외, 마지막 집 포함
        money2 = rob_linear(nums[1:])
        
        return max(money1, money2)
