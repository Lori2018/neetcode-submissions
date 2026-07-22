from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use fixed array of size 26
        def freq(s):
            lowercase = [0 for _ in range(26)]
            for c in s:
                lowercase[ord(c) - ord('a')] += 1
            return lowercase
        sol = []
        m = defaultdict(list)
        for s in strs:
            m[tuple(freq(s))].append(s)
        return list(m.values())