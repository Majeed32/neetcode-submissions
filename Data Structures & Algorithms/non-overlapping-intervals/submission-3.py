class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        row = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < row[1]:
                row[0] = max(row[0], start)
                row[1] = min(row[1], end)
                res += 1
            else:
                row = [start, end]
        return res

        