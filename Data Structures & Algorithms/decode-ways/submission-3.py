class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = dp2 = 0
        dp1 = 1

        for i in range(n-1,-1,-1):
            if s[i] == "0":
                dp = 0
            elif i == n-1:
                dp = 1 if s[i] != "0" else 0
            else:
                one = int(s[i])
                two = int(s[i:i+2])
                if two >= 10 and two <= 26:
                    if i+2>=n:
                        dp = 1
                    else:
                        dp += dp2
                if one > 0:
                    dp += dp1
            dp2 = dp1
            dp1 = dp
            dp = 0
            

        return dp1