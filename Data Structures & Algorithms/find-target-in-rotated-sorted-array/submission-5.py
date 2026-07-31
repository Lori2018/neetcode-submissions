class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[left] < nums[mid]: # left -> mid is sorted
                if target <= nums[mid] and target >= nums[left]:
                    right = mid-1
                else: # target > nums[mid]
                    left = mid+1
            else: # rotation is b/t left and mid - [ 6 1 2 3 4 5 ]
                if target > nums[mid] and target < nums[left]:
                    left = mid+1
                else:
                    right = mid-1
        return left if nums[left] == target else -1
            # if nums[left] < nums[mid] < target => explore mid+1 - right
            # if nums[left] < nums[mid] and target > nums[mid] => explore left - mid-1
            # if nums[right] > target > nums[mid] => explore mid - right
            # if nums[right] < target