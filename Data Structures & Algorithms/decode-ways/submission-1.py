class Solution:
    def numDecodings(self, s: str) -> int:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVQRSYZ"
        n = len(s)
        dp = [0] * n

        for i in range(n-1,-1,-1):
            if i == n-1:
                dp[i] = 1 if s[i] != "0" else 0
                continue 
            one = int(s[i])
            two = int(s[i:i+2])
            if two >= 10 and two <= 26:
                if i+2<n:
                    dp[i] += dp[i+2]
                else:   
                    dp[i] = 1
            if one > 0:
                dp[i] += dp[i+1]
        print(dp)
            

        return dp[0]