from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # alphabetize every str
        groups = defaultdict(list)
        for s in strs:
            alph = "".join(sorted(s))
            groups[alph].append(s)
        return list(groups.values())