def get_max_rob(nums):
    if len(nums) > 1: # nums의 길이가 1인 경우 nums[0] return
        nums[1] = max(nums[0], nums[1]) # nums[0], nums[1] 중 돈이 더 많은 값을 기록

        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
    return nums[-1]

class Solution:
    def rob(self, nums):
        if len(nums) < 4:
            return max(nums)
        ret1 = get_max_rob(nums[1:])
        ret2 = get_max_rob(nums[:-1])
        return max(ret1, ret2)
