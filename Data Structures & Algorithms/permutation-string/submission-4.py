from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window size is len(s1)
        x, y = len(s1), len(s2)
        counts = Counter()
        s1_counts = Counter(s1)

        for i in s2[0:x]:
            counts[i] += 1

        for r in range(x, y+1):
            # print(s2[r-x:r])
            if counts == s1_counts:
                return True
            counts[s2[min(y-1,r)]] += 1
            counts[s2[r-x]] -= 1

        return False