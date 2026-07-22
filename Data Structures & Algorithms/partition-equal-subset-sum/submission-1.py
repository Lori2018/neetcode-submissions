class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        n = len(nums)
        t = sum(nums)/2
        
        def helper(cur, i):
            if cur == t:
                return True 
            if cur > t or i == n:
                return False
            
            return helper(cur + nums[i], i+1) or helper(cur, i+1)

        return helper(0, 0)