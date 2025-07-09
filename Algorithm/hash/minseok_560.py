from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        
        # {누적 합: 등장 횟수}
        prefix_sum_counts = defaultdict(int)
        # 초기화
        prefix_sum_counts[0] = 1
        
        for num in nums:            
            current_sum += num            
            # sum(i, j) = sum(0, j) - sum(0, i-1)
            # k = current_sum - prev_sum  ->  prev_sum = current_sum - k
            if (current_sum - k) in prefix_sum_counts:
                count += prefix_sum_counts[current_sum - k]                        
            prefix_sum_counts[current_sum] += 1
            
        return count
