class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[-1] * m for _ in range(n)]
        def longestFrom(i, j):
            ans = 0
            if i == n or j == m:
                return 0
            if text1[i] == text2[j]:
                if i+1 < n and j+1 < m and dp[i+1][j+1] != -1:
                    ans = 1 + dp[i+1][j+1]
                else:
                    ans = 1 + longestFrom(i+1, j+1)
            else:
                if i+1 < n and j+1 < m and dp[i+1][j+1] != -1:
                    ans = dp[i+1][j+1]
                else: 
                    ans = longestFrom(i+1,j+1)
                if i+1 < n and dp[i+1][j] != -1:
                    ans = max(ans, dp[i+1][j])
                else:
                    ans = max(ans, longestFrom(i+1,j))
                if j+1 < m and dp[i][j+1] != -1:
                    ans = max(ans, dp[i][j+1])
                else:
                    ans = max(ans, longestFrom(i, j+1))
            dp[i][j] = ans
            return ans
        return longestFrom(0, 0)