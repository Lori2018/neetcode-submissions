class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[i]: largest product starting from i

        # -3, 0, 1, -2
        # -3, 0, 0, 0
        # -3, 0, -2, -2
        n = len(nums)
        r = nums[::-1]
        prefix = [nums[0]] * n
        suffix = [nums[-1]] * n
        res = max(nums[0], nums[-1])
        for i in range(1, n): 
            prefix[i] = prefix[i-1] * nums[i]
            suffix[i] = suffix[i-1] * r[i]
            res = max(res,prefix[i], suffix[i], nums[i])
        suffix = suffix[::-1]

        return res