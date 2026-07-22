class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        res = []
        for i in range(len(nums)):
            res.extend(list(([nums[i]] + t for t in self.permute(nums[:i] if i == len(nums) else nums[:i] + nums[i+1:]))))
        return res