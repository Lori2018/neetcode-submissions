from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = defaultdict(set) 
        checked = [0] * len(nums)
        for i in range(len(nums)):
            num[nums[i]].add(i)
        
        maxLen = 0
        curLen = 0
        for i in range(len(nums)):
            if checked[i] == 1:
                continue
            curLen = 1
            nextNum = nums[i] + 1 
            checked[i] = 1
            while nextNum in num:
                curLen += 1
                for j in num[nextNum]:
                    checked[j] = 1;
                nextNum += 1
                
            if curLen > maxLen:
                maxLen = curLen
        return maxLen

        