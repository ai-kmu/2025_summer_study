class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_count = {0: 1}  # 누적합이 0인 경우를 위한 초기값

        for num in nums:
            prefix_sum += num
            diff = prefix_sum - k
            if diff in prefix_count:
                count += prefix_count[diff]
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum] += 1
            else:
                prefix_count[prefix_sum] = 1

        return count
