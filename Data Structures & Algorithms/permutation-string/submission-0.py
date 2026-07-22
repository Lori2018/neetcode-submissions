from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 
        l = 0 
        for r in range(len(s2)):
            if s2[l] not in s1:
                l += 1
            if r-l+1 == len(s1):
                if Counter(s2[l:r+1]) == Counter(s1):
                    return True 
                l += 1
        return False