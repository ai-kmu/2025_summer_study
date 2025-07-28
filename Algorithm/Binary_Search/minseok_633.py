from math import ceil
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # 탐색 범위
        nums = list(range(0, ceil(c**0.5)+1))        
        p, q = 0, len(nums) - 1

        while p <= q:
            sum = nums[p]*nums[p] + nums[q]*nums[q]
            if sum == c:
                return True
            elif sum > c:
                q -= 1
            else:   # sum < c
                p += 1        
                    
        return False

# -------------------------------------------------------------
from math import ceil
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            # 우리가 찾아야 할 b의 제곱 값
            target_squared_b = c - a*a
            # b를 찾기 위한 이진 탐색            
            low, high = 0, ceil(target_squared_b**0.5)
            
            while low <= high:
                mid = (low + high) // 2
                mid_squared = mid * mid
                if mid_squared == target_squared_b:                    
                    return True
                elif mid_squared < target_squared_b:
                    # 값이 더 커야하므로 탐색 범위를 오른쪽으로
                    low = mid + 1
                else: # mid_squared > squared_b
                    # 값이 더 작아야하므로 탐색 범위를 왼쪽으로
                    high = mid - 1
            # 다음 a 값으로
            a += 1
        # 모든 a에 대해 적절한 b를 찾지 못했으면 False
        return False