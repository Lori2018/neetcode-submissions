class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # array of size maxStart val 
        maxStart = max(i[0] for i in intervals)

        # stores end of nums
        numLine = [-1] * (maxStart + 1)

        for start, end in intervals:
            numLine[start] = max(numLine[start], end)
        print(numLine)
        curEnd = -1
        curStart = -1
        res = []
        for i in range(maxStart+1):
            if numLine[i] != -1:
                curEnd = max(curEnd, numLine[i])
                if curStart == -1:
                    curStart = i
            if (i == curEnd or i == maxStart) and curStart != -1: 
                res.append([curStart, curEnd])
                curStart = -1
                curEnd = -1

        # print(numLine)
        return res