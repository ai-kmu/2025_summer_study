class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 끝나는 시간 기준으로 정렬
        intervals.sort(key=lambda x: x[1])

        removed_count = 0
        end_time = intervals[0][1]
    
        for start, end in intervals[1:]:    
            if start < end_time:    
                removed_count += 1
            else:    
                end_time = end

        return removed_count