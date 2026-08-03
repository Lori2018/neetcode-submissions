class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # divide arr in half
        # conquer: base case = if 1 elem, ret that elem
        # combine: 

        # returns max subarray sum
        def helper(left, right):
            if right==left:
                return nums[right]
            elif right == left+1:
                return max(nums[left], nums[right], nums[left]+nums[right])
            mid = (left + right)//2
            leftSum = helper(left, mid)
            rightSum = helper(mid+1, right)
            # ptr part
            leftMax = rightMax = -10001
            tmp = 0
            i = mid
            while i >= left:
                tmp += nums[i]
                i -= 1
                leftMax = max(leftMax, tmp)
            i = mid+1
            tmp = 0
            while i <= right:
                tmp += nums[i]
                i += 1
                rightMax = max(rightMax, tmp)
            return max(leftMax + rightMax, leftSum, rightSum)
        return helper(0, len(nums)-1)