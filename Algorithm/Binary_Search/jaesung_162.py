#162
class Solution(object):
    def findPeakElement(self, nums):
        def recursive(nums):
            if len(nums) == 1:
                return nums
            split = len(nums)//2
            left = recursive(nums[:split])
            right = recursive(nums[split:])

            new = []
            l_i, r_i = 0, 0
            while l_i < len(left) and r_i  < len(right):
                if left[l_i] <= right[r_i]:
                    new.append(left[l_i])
                    l_i += 1
                else:
                    new.append(right[r_i])
                    r_i += 1
            if l_i != len(left):
                new.extend(left[l_i:])
            if r_i != len(right):
                new.extend(right[r_i:])
            return new

        return nums.index(recursive(nums)[-1])
