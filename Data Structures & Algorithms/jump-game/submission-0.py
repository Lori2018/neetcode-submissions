class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canReach = [False] * len(nums)
        canReach[len(nums)-1] = True
        for i in range(len(nums)-1, -1, -1):
            for j in range(nums[i]+1):
                if i+j == len(nums)-1 or canReach[i+j]:
                    canReach[i] = True
                    break
        return canReach[0]