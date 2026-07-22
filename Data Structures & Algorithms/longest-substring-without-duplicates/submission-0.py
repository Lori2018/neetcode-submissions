class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # bit manipulation?
        # sliding window with hashmap
        # right++ until hit smth within hashmap
        # update max
        # left++ until 

        # use array with ascii codes
        # same amt of time as hashmap
        chars = {}
        left = 0
        right = 0
        length = 0
        maxLength = 0
        while right < len(s):
            while s[right] in chars:
                del chars[s[left]]
                left += 1
                length -= 1
            chars[s[right]] = 1
            right += 1
            length += 1
            maxLength = max(length, maxLength)
        return maxLength
