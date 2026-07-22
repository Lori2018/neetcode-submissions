class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [10001] * amount

        for i in range(amount+1):
            for c in coins:
                if i-c == 0:
                    dp[i] = 1
                elif i-c>=0 and dp[i-c] < dp[i]:
                    dp[i] = dp[i-c] + 1
        return dp[amount] if dp[amount] < 10001 else -1