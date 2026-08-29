"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in range(len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            time.append((start, 1))
            time.append((end, -1))
        time.sort()
        maxRooms = 0
        count = 0
        for t in time:
            count += t[1]
            maxRooms = max(maxRooms, count)
        return maxRooms
        