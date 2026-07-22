from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = []
        sol.append(reduce(lambda x, y: x * y, nums[1:]))

        numZeroes = 0
        index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                numZeroes += 1
                index = i
        
        product = 1
        if numZeroes == 1:
            for i in range(len(nums)):
                if i != index:
                    product *= nums[i]

        for i in range(1, len(nums)):
            if numZeroes == 1:
                if i == index:
                    sol.append(product)
                else:
                    sol.append(0)
            elif numZeroes > 1:
                sol.append(0)
            else:
                sol.append(int(sol[-1] * nums[i - 1] / nums[i]))

        return sol

            