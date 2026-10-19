class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mins, maxes = [prices[0]] * n, [prices[-1]] * n
        for i in range(n):
            if i == 0:
                continue
            mins[i] = min(mins[i-1], prices[i])
            maxes[n-i-1] = max(maxes[n-i], prices[n-i-1])
        return max([x-y for x, y in zip(maxes, mins)])
