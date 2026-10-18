class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set()
        for n in nums:
            if n in x:
                return True
            x.add(n)
        return False