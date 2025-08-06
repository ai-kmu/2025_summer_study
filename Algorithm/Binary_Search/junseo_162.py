class Solution(object):
    def findPeakElement(self, nums):

        n = len(nums)
        
        for i in range(n):
            left = float('-inf') if i == 0 else nums[i - 1] # i가 가장 왼쪽 값일 때 왼쪽 -inf 조건 추가 
            right = float('-inf') if i == n - 1 else nums[i + 1] # i가 가장 오른쪽 값일 때 오른쪽 -inf 조건 추가

            if nums[i] > left and nums[i] > right:
                return i  # peak를 찾으면 바로 반환 
        