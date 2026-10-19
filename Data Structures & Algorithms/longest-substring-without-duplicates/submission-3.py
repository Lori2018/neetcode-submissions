class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = -1
        counts = defaultdict(int)
        res = 0
        while right < len(s)-1:
            right += 1
            counts[s[right]] += 1
            while counts[s[right]] == 2:
                # increment left till all counts are 1
                counts[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res