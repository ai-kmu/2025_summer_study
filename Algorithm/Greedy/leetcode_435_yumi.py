class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])  # 끝나는 시간 기준 정렬
        end = float('-inf')  # 아직 아무 구간도 선택하지 않았을 때 초기값
        count = 0

        for start, finish in intervals:
            if start < end:
                # 이 구간은 앞에 선택된 구간이랑 겹침 → 제거 필요
                count += 1
            else:
                # 안 겹침 → 이 구간 선택! end 시간 갱신
                end = finish

        return count
                
