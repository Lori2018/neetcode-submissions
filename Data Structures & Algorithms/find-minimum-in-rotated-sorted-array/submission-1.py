class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        min_ = 1001
        while left<right:
            # need to check if mid > front
            # rotated to the right
            mid = (left+right)//2
            min_ = min(nums[mid], min_)
            if nums[mid] > nums[left]:
                min_ = min(min_, nums[left])
                # new range is mid-right
                left = mid+1
            else: # nums[left] > nums[mid] --> the min element must be in this range
                min_ = min(min_, nums[right])
                right = mid-1
        return min(min_, nums[left])
