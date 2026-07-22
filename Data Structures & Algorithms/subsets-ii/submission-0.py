class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        nums.sort()
        print(nums)

        def dfs(i):
            print(f"called on {i}")
            if i == len(nums):
                return [[]]
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            res = []
            temp = dfs(i+1)
            print(f"call returned {temp}")
            for t in temp:
                for j in range(counts[nums[i]]+1):
                    print(j)
                    res.append([nums[i]] * j + t)
            return res
        return dfs(0)

            