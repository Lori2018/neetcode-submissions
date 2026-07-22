class Solution:
    def rob(self, nums: List[int]) -> int:

        def dp(arr):
            n = len(arr)
            m = [0] * n

            for i in range(n-1, -1, -1):
                if i == n-1:
                    m[i] = arr[i]
                elif i == n-2:
                    m[i] = max(arr[i], arr[i+1])
                else: 
                    m[i] = max(arr[i] + m[i+2], m[i+1])
            return m[0]

        if len(nums) < 3:
            return max(nums)
        return max(dp(nums[1:]), dp(nums[:-1]))