class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # use recursion 
        if len(nums) == 0:
            return [nums]
        
        sets = self.subsets(nums[1:])
        res = []

        for s in sets:
            res.append(s)
            res.append([nums[0]] + s) 
        return res