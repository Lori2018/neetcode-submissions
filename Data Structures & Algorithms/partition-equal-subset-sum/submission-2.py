class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        n = len(nums)
        t = sum(nums)//2
        memo = [[-1] * (t + 1) for _ in range(n+1)]
        
        def helper(cur, i):
            if cur == t:
                return True 
            if cur > t or i == n:
                return False
            if memo[i][cur] != -1:
                return memo[i][cur]

            
            memo[i][cur] = helper(cur + nums[i], i+1) or helper(cur, i+1)
            return memo[i][cur]

        return helper(0, 0)