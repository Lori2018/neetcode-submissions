from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]
        for i in range(1, len(nums)):
            prefixes.append(nums[i - 1] * prefixes[i - 1])

        suffixes = [1]
        numsReversed = nums[::-1]
        for i in range(1, len(nums)):
            suffixes.append(numsReversed[i - 1] * suffixes[i - 1])
        suffixes = suffixes[::-1]

        return [prefixes[i] * suffixes[i] for i in range(0, len(nums))]