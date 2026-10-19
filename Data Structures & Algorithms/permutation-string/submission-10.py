class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        s1_freq = [0] * 26
        cur = [0] * 26

        # make frequency arrs
        for i in range(n):
            s1_freq[ord(s1[i])-ord("a")] += 1
            cur[ord(s2[i])-ord("a")] += 1

        for i in range(m-n+1):
            if s1_freq == cur:
                return True
            cur[ord(s2[i])-ord("a")] -= 1
            if i+n<m:
                cur[ord(s2[i+n])-ord("a")] += 1
        return False