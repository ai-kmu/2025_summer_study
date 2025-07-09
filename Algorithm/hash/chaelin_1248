class Solution(object):
    def numberOfSubarrays(self, nums, k):
        count = 0
        prefix_sum = 0
        d = {0: 1}

        for num in nums:
            if num % 2 == 1:
                prefix_sum += 1

            if prefix_sum - k in d: 
                count += d[prefix_sum - k]

            if prefix_sum not in d:
                d[prefix_sum] = 1
            else:
                d[prefix_sum] += 1

        return count
