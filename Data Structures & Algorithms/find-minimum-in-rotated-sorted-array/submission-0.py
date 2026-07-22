class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0 
        hi = len(nums) - 1
        while lo < hi:
            mid = (hi - lo) // 2 + lo
            # if mid > hi, min is def in right side 
            # if mid < hi, min is in left side
            if (mid - 1 >= 0 and nums[mid] < nums[mid - 1]) and (mid + 1 < len(nums) and nums[mid] < nums[mid + 1]):
                return nums[mid]
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
        return nums[lo]