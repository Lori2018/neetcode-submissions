class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] represents max money you can rob starting from i
        n = len(nums)

        dp = [0] * n

        for i in range(n-1, -1, -1):
            if i == n-1:
                dp[i] = nums[i]
            elif i == n-2:
                dp[i] = max(nums[i], nums[i+1])
            else:
                # if include i: nums[i] + 
                dp[i] = max(nums[i] + (0 if i+2 >= n else dp[i+2]), dp[i+1])
                
        if n == 1:
            return dp[0]
        return max(dp[0], dp[1])