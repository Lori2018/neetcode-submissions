class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # add up all the numbers
        n = len(nums)
        x = 0
        for i in range(n):
            x += nums[i]
        return (n * (n+1)) // 2 - x