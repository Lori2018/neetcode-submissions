class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [101] * len(nums)
        res[len(nums)-1] = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] >= 1:
                res[i] = min([101] + [res[min(len(nums)-1,i+j)] for j in range(1, nums[i]+1)]) + 1
        return res[0]
                