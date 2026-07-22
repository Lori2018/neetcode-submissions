class Solution:
    def countSubstrings(self, s: str) -> int:
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        dp = [0] * n
        l = r = 0

        for i in range(n):
            dp[i] = min(r-i, dp[l+(r-i)]) if i < r else 0
            while i+dp[i]+1<n and i-dp[i]-1>=0 and t[i+dp[i]+1]==t[i-dp[i]-1]:
                dp[i] += 1
            if i+dp[i] > r:
                l,r = i-dp[i], i+dp[i]

        res = 0
        for i in dp:
            res += (i+1)//2
        return res