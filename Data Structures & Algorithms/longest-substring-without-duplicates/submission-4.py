class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a set to make faster
        l = 0
        r = -1
        counts = set()
        res = 0
        while r < len(s)-1:
            r += 1
            while s[r] in counts:
                counts.remove(s[l])
                l += 1
            counts.add(s[r])
            res = max(res, r-l+1)
        return res