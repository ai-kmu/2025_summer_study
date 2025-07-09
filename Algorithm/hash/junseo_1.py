# 560. Subarray Sum Equals K
class Solution(object):
    def subarraySum(self, nums, k):

        count = 0 # 정답
        current_sum = 0 # 현재 누적합 
        prefix_count = {0 : 1} # 초기값: 합이 0인 경우 1번 있다고 간주

        for num in nums:
            current_sum += num
            # sum[j] - sum[i] = k 일 때를 찾아야 함 
            # current_sum - k = sum[i] 성립 
            # 이 sum[i]가 나온 적이 있다면 해당 그만큼 k를 만족하는 구간이 존재했다는 뜻이 됨 
            # 이전 누적합에 대해서 누적합을 k/ 등장 횟수를 v 
            if current_sum - k in prefix_count:
                # 현재 누적합에서 k를 뺀 값이 과거에 몇번 나왔는지 확인
                # 그 개수만큼 구간이 존재하니까 카운트에 추가 
                count += prefix_count[current_sum -k]
            # 현재 누적합을 prefix_count에 기록
            # 처음 등장하는 값이라면 keyerror 발생하니까 
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1
        return count