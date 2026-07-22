class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        # 9, 1, 4, 2, 3, 3, 7
        # 1, 4, 2, 3, 2, 2, 1

        # O(n^2): for each i, iterate through rest of array to find next highest, 
        # use stack to keep track of numbers?

        for i in range(n-2,-1,-1):
            for j in range(i, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
                elif nums[j] == nums[i]:
                    dp[i] = max(dp[j], dp[i])
        print(dp)
        return max(dp)