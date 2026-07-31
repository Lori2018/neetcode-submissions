class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(rate):
            res = 0
            for p in piles:
                res += math.ceil(p/rate)
            return res
        # range starts at [1, max in piles]
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            cur_h = hours(mid)
            if cur_h > h: # need to increase rate
                left = mid+1
            elif cur_h <= h:
                right = mid
        return left