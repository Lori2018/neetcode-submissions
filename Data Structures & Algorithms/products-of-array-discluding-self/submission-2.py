class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1, 1, 2, 8]
        # postfix = [48, 24, 6, 1]
        n = len(nums)
        prefix = [1 for _ in range(n)]
        postfix = prefix.copy()

        for i in range(n):
            if i >= 1:
                prefix[i] = prefix[i-1] * nums[i-1]
            if n-i-1 < n-1:
                postfix[n-i-1] = postfix[n-i] * nums[n-i]
        return [prefix[i] * postfix[i] for i in range(n)]