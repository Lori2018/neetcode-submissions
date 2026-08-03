class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -10001
        cur = 0
        for x in nums:
            cur += x
            res = max(cur, res)
            if cur < 0:
                cur = 0
        return res