class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # iterate through, maintain end dist 
        goal = 0
        for i in range(len(nums)): 
            if i > goal:
                return False
            goal = max(i+nums[i], goal)
        
        return True