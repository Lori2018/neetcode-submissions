class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        maxSum = -1000
        for num in nums:
            cur = max(num, num + cur)
            maxSum = max(maxSum, cur)

        return maxSum