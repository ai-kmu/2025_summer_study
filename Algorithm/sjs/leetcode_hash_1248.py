class Solution: #홀 수가 k개인 연속된 배열 찾기
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        length = len(nums)

        def MostOdd(numOdd):
            count = 0
            left = 0
            for i in range(length):
                if nums[i] % 2 == 1:
                    numOdd -= 1
                while numOdd < 0:
                    if nums[left] % 2 == 1:
                        numOdd += 1
                    left += 1
                count += i - left + 1
            return count

        return MostOdd(k) - MostOdd(k-1)
