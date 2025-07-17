def subsets(self, nums: List[int]) -> List[List[int]]:
    length = len(nums)
    result = []
    repeat = 2 ** length

    for i in range(repeat):
        subset = []
        for j in range(length):
            if i & (1 << j):
                subset.append(nums[j])
        result.append(subset)

    return result
