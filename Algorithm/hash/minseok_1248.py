from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        odd_count = 0
    
        # {홀수 총 개수: 등장 횟수}
        freq = defaultdict(int)
        # 초기화
        freq[0] = 1

        for num in nums:        
            if num % 2 != 0:
                odd_count += 1
            # odd 개수(i, j) = odd 개수(0, j) - odd 개수(0, i-1)
            # k = odd_count - 이전 odd_count  ->  이전 odd_count = odd_count - k
            if (odd_count - k) in freq:
                count += freq[odd_count - k]            
            freq[odd_count] += 1

        return count
