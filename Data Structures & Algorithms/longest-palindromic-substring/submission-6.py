class Solution:
    def longestPalindrome(self, s: str) -> str:
        initial = s
        # aba  -> a#b#a
        # abba -> a#b#b#a
        # 
        # a#b#c#d#b#d#c - 12
        # 0, 12 -> 

        # now all palindrome lengths are ODD
        # 2 ptr solution 
        # while it is a palindrome, increase length
        r = l = 0
        s = '#' + '#'.join(s) + '#'
        n = len(s)
        dp = [0] * n
        for i in range(n):
            # try to expand out 
            if i < r:
                dp[i] = min(r-i, dp[l+(r-i)]) # otherwise overlapping palindromes would make this incorrect
            while i-dp[i]-1>= 0 and i+dp[i]+1<n and s[i-dp[i]-1] == s[i+dp[i]+1]:
                dp[i] += 1
            if i+dp[i] > r:
                l, r = i-dp[i], i+dp[i]

        res = 0 
        resLen = 0
        for i, val in enumerate(dp):
            if val > resLen:
                resLen = val
                res = i
        
        return initial[(res-resLen) // 2: (res-resLen) // 2 + resLen]