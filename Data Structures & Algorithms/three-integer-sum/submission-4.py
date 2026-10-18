from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # tuples (i, j, k) st i<j<k
        # store remainder map for k -> 1 pass
        #   remainder -> index
        # {1: 0, 0: 1, -1: 2, -2: 3, 1: 4, 4: 5}
        # every possible i, j combo, check if it's in the map
        n = len(nums)
        sol = set()
        remainders = defaultdict(set) # remainder -> index
        for i in range(n):
            remainders[-nums[i]].add(i)

        for i in range(n):
            for j in range(n):
                if i >= j:
                    continue
                s = nums[i] + nums[j]
                kset = remainders[s]
                if len(kset) == 1 and (i in kset or j in kset):
                    continue
                elif len(kset) == 2 and i in kset and j in kset:
                    continue
                elif len(kset) == 0:
                    continue
                # print(i, j, kset)
                pos = sorted((nums[i], nums[j], -s))
                sol.add(tuple(pos))
        # convert to list of lists
        final_sol = []
        for s in sol:
            final_sol.append(list(s))
        return final_sol