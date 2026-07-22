class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        n = len(intervals)
        res = []
        while i < n - 1:
            print(f"considering {intervals[i]} and {intervals[i+1]}")
            if intervals[i][1] >= intervals[i+1][0]:
                print("merge")
                intervals[i+1] = [min(intervals[i][0], intervals[i+1][0]), max(intervals[i][1], intervals[i+1][1])]
                print(intervals[i+1])
            else:
                res.append(intervals[i])
            i += 1
        res += [intervals[i]]
        return res