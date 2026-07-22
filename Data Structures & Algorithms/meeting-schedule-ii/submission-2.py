"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: (x.start, -x.end))
        # use a stack
        for interval in intervals:
            print(f"{interval.start}, {interval.end}")
        # count number of overlapping
        res = 0
        # add end times to queue
        heap = []
        length = 0
        for interval in intervals:
            heapq.heappush(heap, interval.end)
            length += 1
            while interval.start >= heap[0]:
                heapq.heappop(heap)
                length -= 1
            res = max(length, res)
            # print(q)
        return res