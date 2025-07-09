# 배열의 특정 구간의 합이 k가 되는 경우의 수를 구하는 문제
# Prefix Sum 활용
class Solution(object):
    def subarraySum(self, nums, k):
        result = 0
        prefix_sum = 0
        d = {0: 1}

        for i in nums:
            prefix_sum += i
            
            if prefix_sum - k in d:
                result += d[prefix_sum - k]

            if prefix_sum not in d:
                d[prefix_sum] = 1
            else:
                d[prefix_sum] += 1

        return result
