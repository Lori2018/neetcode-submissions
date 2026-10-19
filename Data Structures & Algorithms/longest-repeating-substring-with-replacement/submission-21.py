class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        # return longest repeating subseuqence with letter 
        def helper(letter):
            # "ABAABBBAAB"
            # l,r denote current subsequence
            res = 0
            l = 0
            k_used = 0
            for r in range(n):
                # if k == k_used, increment l until k_used < k
                if s[r] != letter:
                    k_used += 1
                while k_used > k:
                    if s[l] != letter:
                        k_used -= 1
                    l += 1
                res = max(r-l+1, res)
            return res
        res = 0
        for l in set(s):
            res = max(res, helper(l))
        return res