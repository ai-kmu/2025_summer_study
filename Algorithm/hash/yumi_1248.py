class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def at_most_k_odds(k):
            left = 0
            cnt = 0
            odd_count = 0
            
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd_count += 1
                
                while odd_count > k:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1
                
                cnt += right - left + 1
            return cnt

        return at_most_k_odds(k) - at_most_k_odds(k - 1)

  # 홀수가 k개가 최대인 베열 수에서 k-1개가 최대인 배열 수를 뺀다.
