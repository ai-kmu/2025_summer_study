# 1248. Count Number of Nice Subarrays
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        
        count = 0 # 정답
        current_odd_c = 0 # 현재 누적 홀수 개수
        prefix_count = {0 : 1} # k: 누적 홀수 개수 v: 누적 홀수개수 몇번 나왔는지

        for num in nums:
            if num % 2 != 0: # 현재 구간에서 홀수일때만 개수를 추가 
                current_odd_c += 1 # 현재 누적 홀수 개수
            # 누적합과 다르게 누적 홀수 개수의 차를 계산하면 됨 
            # 현재 누적 홀수 개수 - 이전 누적 홀수 개수 = k를 찾아야 함 
            # 현재 누적 홀수 개수 - k = 이전 누적 홀수 개수 
            # 이전 누적 홀수가 몇 번 등장했는지 알면 k를 만족하는 구간 개수를 알 수 있음 
            if current_odd_c - k in prefix_count: 
                count += prefix_count[current_odd_c - k] # 있다면 count에 + 1 
            # 현재 누적 홀수 개수라 prefix_count에 추가
            # 이미 있다면 +1, 아니라면 해당 값 초기화 후 + 1
            prefix_count[current_odd_c] = prefix_count.get(current_odd_c, 0) + 1 
        return count 







