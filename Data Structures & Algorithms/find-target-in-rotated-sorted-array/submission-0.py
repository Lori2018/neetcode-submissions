class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        mid = hi // 2

        while lo < hi:
            if target == nums[mid]:
                return mid
            elif nums[mid] > nums[hi]:
                if target > nums[mid] or target <= nums[hi]:
                    lo = mid + 1
                else: 
                    hi = mid - 1
            elif nums[lo] > nums[mid]:
                if target >= nums[lo] or target < nums[mid]: 
                    hi = mid - 1
                else: 
                    lo = mid + 1
            else: 
                if target > nums[mid]: 
                    lo = mid + 1
                else: 
                    hi = mid - 1
            mid = (hi - lo) // 2 + lo
        return mid if target == nums[mid] else -1
