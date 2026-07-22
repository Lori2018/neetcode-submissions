from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # store consecutive seq of numbers in a map 
        # start number -> length of consecutive
        # need reverse map too
        start = {} # start num -> length
        end = {} # end num -> length
        for n in nums:
            if n in end or n in start:
                continue
            elif n-1 in end and n+1 in start:
                print("here")
                l1 = start[n+1]
                l2 = end[n-1]
                del end[n-1]
                del start[n+1]
                newLength = l2 + l1 + 1
                start[n-l2] = newLength
                end[n+l1] = newLength
            elif n-1 in end:
                length = end[n-1]
                start[n-length] += 1
                end[n] = length + 1
                del end[n-1]
            elif n+1 in start:
                length = start[n+1]
                end[n+length] += 1
                start[n] = length + 1
                del start[n+1]
            else:
                start[n] = 1
                end[n] = 1
            # print("start: " + str(start))
            # print("end: " + str(end))
        ans = 0
        for _, v in start.items():
            ans = max(ans, v)
        return ans