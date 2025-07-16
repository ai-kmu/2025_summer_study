class Solution(object):
    def subsets(self, nums):

        result = []  # 최종 결과 (모든 부분집합)을 저장할 리스트

        def backtrack(start, path):
            # 현재까지 구성한 부분집합을 결과에 추가
            # path[:]로 복사하여 저장해야 이후 path 변경이 영향을 안 줌
            result.append(path[:])

            # start 인덱스부터 남은 원소들을 하나씩 추가하며 재귀적으로 부분집합 확장
            for i in range(start, len(nums)):
                # 현재 원소 nums[i]를 부분집합에 포함
                path.append(nums[i])

                # 다음 인덱스(i+1)부터 재귀적으로 더 깊은 부분집합 생성
                backtrack(i + 1, path)

                # 백트래킹: 마지막에 추가한 원소를 제거하여 원래 상태로 복구
                path.pop()

        # 부분집합 생성을 위한 백트래킹 시작
        # start는 현재 위치, path는 현재까지 선택된 원소들
        backtrack(0, [])

        return result