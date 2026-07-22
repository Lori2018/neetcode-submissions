class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ""
        for s in strs:
            sol += s
            sol += ";"
        return sol
    def decode(self, s: str) -> List[str]:
        sol = []
        for i in range(s.count(";")):
            x = s.find(";")
            sol += [s[0:x]]
            s = s[x + 1:]
        return sol
