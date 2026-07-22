import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 0
        for i in piles:
            if i > k:
                k = i

        # monotonically decreasing
        hiK = k
        loK = 0

        while loK < hiK and k != 1:
            hours = 0
            k = int((hiK - loK) / 2 + loK)
            for p in piles:
                hours += (p + k - 1) // k
            if hours > h:
                loK = k + 1
            else: 
                hiK = k
        return int(hiK)