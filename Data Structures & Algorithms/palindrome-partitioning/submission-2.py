class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        def isPali(x,y):
            while x < y:
                if s[x] != s[y]:
                    return False
                x += 1
                y -= 1
            return True
        def dfs(j,i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return
            if isPali(j,i):
                part.append(s[j:i+1])
                dfs(i+1,i+1)
                part.pop()
            dfs(j,i+1)

        dfs(0,0)
        return res