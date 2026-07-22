class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find max ending of interval <= newInterval's beginning
        # find min beginning of interval >= newInterval's end 
        a = 0
        while a < len(intervals) and intervals[a][1] < newInterval[0]:
            a += 1
        intervals.insert(a, newInterval)
        
        # merge left 
        while a-1 > 0 and intervals[a-1][0] >= intervals[a][0]:
            interval = [min(intervals[a][0], intervals[a-1][0]), max(intervals[a-1][0], intervals[a][0])]
            intervals[a-1] = interval
            intervals.remove(intervals[a])
        # merge right
        while a < len(intervals) - 1 and intervals[a+1][0] <= intervals[a][1]:
            interval = [min(intervals[a][0], intervals[a+1][0]), max(intervals[a+1][1], intervals[a][1])]
            intervals[a+1] = interval
            intervals.remove(intervals[a])

        return intervals