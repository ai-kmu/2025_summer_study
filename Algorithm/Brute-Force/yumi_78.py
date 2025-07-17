class Solution(object):
    def subsets(self, nums):
        
        length = len(nums)
        solution_set = []
        for i in range(1 << length):
            subset = []
            for j in range(length):

                if (i >> j) & 1:
                    subset.append(nums[j])
            solution_set.append(subset)

        return solution_set 
            
