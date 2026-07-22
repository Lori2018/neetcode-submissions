class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = set()
        nums.sort()

        for mid in range(1, len(nums) - 1):
            left = 0
            right = len(nums) - 1
            while left < right and left < mid and mid < right:
                if nums[mid] + nums[left] + nums[right] == 0:
                    sol.add((nums[left], nums[mid], nums[right]))
                    if left + 1 == mid:
                        left = mid + 1
                    else: 
                        left += 1
                    if right - 1 == mid:
                        right = mid - 1
                    else: 
                        right -= 1
                elif nums[mid] + nums[left] + nums[right] < 0:
                    if left + 1 == mid:
                        left = mid + 1
                    else:
                        left += 1
                else:
                    if right - 1 == mid:
                        right = mid - 1
                    else: 
                        right -= 1
        return [list(tup) for tup in sol]