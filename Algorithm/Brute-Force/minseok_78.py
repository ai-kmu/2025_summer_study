class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:        
        result = []   
        current_searching_subset = []
        
        def backtrack(start_index):
            result.append(current_searching_subset[:])
            
            for i in range(start_index, len(nums)):                
                current_searching_subset.append(nums[i])
                # 다음 원소를 시작으로 탐색
                backtrack(i + 1)
                # 백트래킹 - 추가했던 원소 삭제
                current_searching_subset.pop()
        
        backtrack(0)

        return result