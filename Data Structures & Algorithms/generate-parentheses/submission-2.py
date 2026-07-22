class Solution:
    n = 0
    sol = []
    # open, close vars, increment both (2 paths) unless close > open 
    # if length == 2n, add to result
    def generateParenthesis(self, n: int) -> List[str]:
        self.sol = []
        self.n = n
        self.gen("", 0, 0)
        return self.sol

    def gen(self, s: str, o: int, c: int):
        if len(s) == 2 * self.n and o == c:
            self.sol.append(s)
            return
        elif len(s) < 2 * self.n:
            self.gen(s + "(", o + 1, c)
            if c < o:
                self.gen(s + ")", o, c + 1)