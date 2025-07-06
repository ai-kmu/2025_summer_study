class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {0: 1}
        cumulative_sum = 0
        count = 0

        for right in range(len(nums)):
            cumulative_sum += nums[right]
            result = cumulative_sum - k
            count += sum_dict.get(result, 0)
            sum_dict[cumulative_sum] = sum_dict.get(cumulative_sum, 0) + 1

        return count
