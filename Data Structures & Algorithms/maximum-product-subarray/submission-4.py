class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        maxPos = nums[0]
        minNeg = nums[0]
        res = nums[0]

        for i in range(1, n):
            print(f"before {i}: minNeg: {minNeg}, maxPos: {maxPos}")
            temp = max(nums[i], nums[i] * maxPos, minNeg * nums[i])
            minNeg = min(nums[i], nums[i] * minNeg, nums[i] * maxPos)
            maxPos = temp
            res = max(minNeg, maxPos, res)
            print(f"i = {i}: minNeg: {minNeg}, maxPos: {maxPos}")
        return res