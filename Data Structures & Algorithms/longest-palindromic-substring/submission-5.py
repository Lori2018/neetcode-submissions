class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i]: longest length to the right from i
        n = len(s)
        resLen = 0
        res = 0
        even = False
        
        for i in range(n):
            right = i
            left = i
            # odd length
            while right < n and left >= 0 and s[left] == s[right]:
                if right - left + 1 > resLen:
                    resLen = right - left + 1
                    res = i
                    even = False
                left -= 1
                right += 1
            
            # even length
            right = i+1
            left = i
            while right < n and left >= 0 and s[left] == s[right]:
                if right - left + 1 > resLen:
                    resLen = right - left + 1
                    res = i
                    even = True
                left -= 1
                right += 1
        
        return s[res-resLen//2:res+resLen//2+1] if not even else s[res-resLen//2 + 1: res+resLen//2+1]