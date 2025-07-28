class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left_index, right_index = 0, len(nums) - 1

        while left_index < right_index:
            # left와 right 길이
            n = right_index - left_index + 1
            # 중앙 인덱스 = 길이//2 + 시작 인덱스
            mid_index = n//2 + left_index
            # 오른쪽이 더 크면 오름차순으로 간주하여 피크도 오른쪽에 있다고 생각
            if nums[mid_index-1] < nums[mid_index]:
                left_index = mid_index
            # 왼쪽이 더 크거나 같으면 내림차순으로 간주하여 피크도 왼쪽에 있다고 생각
            else:
                right_index = mid_index - 1
        # while문 빠져 나왔다는 것은 left_index == right_index
        return left_index