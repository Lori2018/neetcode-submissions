from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # goal: O(mn)
        # iterating thru letters for each word
        # can't sort each word
        # make charMap of each str, add to list (index is groupNum)
        # map[groupNum] = wordList
        # somehow use prime numbers to give score
        # map[primeNumber] = list of words
        # only need max 26 prime numbers
        # can generate 26 prime numbers in constant time
        # 1 + 3 + 5
        # 1 + 5 + 7 = 9 + 3
        def freq(s):
            counts = defaultdict(int)
            for c in s:
                counts[c] += 1
            return counts

        sol = []
        maps = []
        for s in strs:
            f = freq(s)
            try:
                i = maps.index(f)
            except ValueError:
                i = len(maps)
                sol.append(list())
                maps.append(f)
            # insert in sol list
            sol[i].append(s)

        return sol