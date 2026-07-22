class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        length = [1] * n
        for i in range(n-1,-1,-1):
            radius = 0
            left = right = i
            while left >= 0 and right < n and s[right] == s[left]:
                res += 1
                radius += 1
                left -= 1
                right += 1
            left = i
            right = i+1
            radius = 0
            while left >= 0 and right < n and s[right] == s[left]:
                res += 1
                left-=1
                right += 1
    
        return res