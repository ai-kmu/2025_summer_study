class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # 첫번째 집 털 때
        max1 = self.func(nums[:-1])
        
        # 첫번째 집 건너 뛰고 털 때
        max2 = self.func(nums[1:])
        
        return max(max1, max2)

    def func(self, nums: List[int]) -> int:
        # rob1: n을 기준으로 2칸 뒤까지 털었을 때 <- +n을 할 수 있음
        # rob2: n을 기준으로 1칸 뒤까지 털었을 때
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            # n+1 기준으로 rob2가 rob1 자리가 됨
            rob1 = rob2
            # n+1 기준으로 temp가 rob1 자리가 됨
            rob2 = temp
        return rob2