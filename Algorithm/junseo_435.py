class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        
        # 각 구간의 끝나는 시간을 기준으로 오름차순 정렬
        # 끝나는 시간이 빠른 구간을 먼저 선택하면, 이후에 더 많은 구간과 겹치지 않고 선택할 수 있는 기회가 생김
        intervals.sort(key=lambda x: x[1]) # 끝나는 값 x[1]을 기준으로 오름차순 

        end = [] # 선택한 구간의 전체 리스트
        count = 0 # 겹치는 구간 수

        for i in range(len(intervals)):
            if not end:
                end.append(intervals[i]) # 첫 interval은 무조건 append
            else:
                # 전체 선택 구간에서의 마지막 요소만 확인하면 됨
                # 이전 선택의 마지막 구간의 끝 부분
                pre_end = end[-1][1] 

                # 현재 interval의 시작 부분
                start = intervals[i][0]
                
                # 겹치는 구간 발생
                if pre_end > start:
                    count += 1 # 겹쳤으니까 횟수 증가
                # 겹치지 않는다면
                else:
                    end.append(intervals[i]) # 선택 구간에 append

        return count
