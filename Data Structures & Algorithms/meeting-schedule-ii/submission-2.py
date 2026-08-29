from typing import List
import heapq

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals by their start time
        intervals.sort(key=lambda x: x.start)
        
        # Initialize a min-heap
        heap = []
        
        # Add the first meeting's end time to the heap
        heapq.heappush(heap, intervals[0].end)
        
        # Iterate over the rest of the intervals
        for i in range(1, len(intervals)):
            # If the room that finishes earliest is free (i.e., the current meeting starts after or when the earliest meeting ends)
            if intervals[i].start >= heap[0]:
                # Remove the earliest ending meeting from the heap (freeing up a room)
                heapq.heappop(heap)
                
            # Add the current meeting's end time to the heap
            heapq.heappush(heap, intervals[i].end)
        
        # The size of the heap is the number of rooms required
        return len(heap)
