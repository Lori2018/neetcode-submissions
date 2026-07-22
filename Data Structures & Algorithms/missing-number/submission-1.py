class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0 1 2 3
        # 0, 01, 10, 11

        # 1 2 3
        # 01, 10, 11 -> 01 ^ 10 ^ 11 = 11 ^ 11 = 00
        # 0, 2, 3
        # 0, 10, 11 -> 0 ^ 10 ^ 11 = 10 ^ 11 = 01

        # 0, 1, 3
        # 00, 01, 11 -> 01 ^ 11 = 10

        # 0, 2
        # 00 ^ 10 = 10
        # 1 ^ 1 ^ 2 ^ 2 ^ 3 ^ 4 ^ 4 ^ 5 ^ 5
        # add up all the numbers
        n = len(nums)
        x = n
        for i in range(n):
            x ^= i ^ nums[i]
        return x