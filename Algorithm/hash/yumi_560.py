class Solution(object):
    def subarraySum(self, nums, k):
        total = 0
        prefix_sum = 0 
        d = {0: 1}

        for i in nums:
            prefix_sum = prefix_sum + i

            if prefix_sum - k in d:
                total += d[prefix_sum - k]

            # 딕셔너리의 값 채워 넣기
            if prefix_sum not in d:
                d[prefix_sum] = 1
            else:
                d[prefix_sum] = d[prefix_sum] + 1

        return total
