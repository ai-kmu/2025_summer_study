class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])

        now_end = float('-inf')
        count = 0

        for interval in intervals:
            if interval[0] >= now_end:
                count += 1
                now_end = interval[1]

        return len(intervals) - count
