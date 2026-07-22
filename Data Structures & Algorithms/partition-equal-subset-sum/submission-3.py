class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        t = sum(nums) // 2
        dp = 1 << 0

        for num in nums:
            # add num to every achievable sum
            dp |= dp << num
        
        return (dp & (1 << t)) != 0