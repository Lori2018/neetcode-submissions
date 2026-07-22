from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x, y = len(s1), len(s2)
        counts = Counter(s2[0:x])
        s1_counts = Counter(s1)

        if counts == s1_counts:
            return True

        for r in range(x, y):
            counts[s2[r]] += 1
            counts[s2[r-x]] -= 1
            if counts == s1_counts:
                return True

        return False