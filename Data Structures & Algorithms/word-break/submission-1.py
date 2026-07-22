class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n

        for i in range(n, -1, -1):
            for word in wordDict:
                if s[i:i+len(word)] == word and i+len(word) >= n:
                    dp[i] |= True
                elif s[i:i+len(word)] == word and dp[i+len(word)]:
                    dp[i] |= True
        return dp[0]