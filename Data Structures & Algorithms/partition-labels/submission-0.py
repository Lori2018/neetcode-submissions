class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # use Counter instead
        counts = Counter(s)
        chars = set()
        res = []
        prev = -1
        for i in range(len(s)):
            x = s[i]
            if len(chars) == 0 or x not in chars:
                chars.add(x)
            counts[x] -= 1
            if counts[x] == 0:
                chars.remove(x)
            if len(chars) == 0:
                res.append(i-prev)
                prev = i
        return res
            