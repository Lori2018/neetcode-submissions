class Solution:
    delim = '\x8A'

    def encode(self, strs: List[str]) -> str:
        sol = ""
        for s in strs:
            sol += (s + self.delim)
        return sol

    def decode(self, s: str) -> List[str]:
        sol = []
        word = ""
        for c in s:
            if c == self.delim:
                sol.append(word)
                word = ""
                continue
            word += str(c)
        return sol