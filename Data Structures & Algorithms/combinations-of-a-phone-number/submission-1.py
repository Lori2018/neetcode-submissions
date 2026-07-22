class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        chars = ["a b c", "d e f", "g h i", "j k l", "m n o", "p q r s", "t u v", "w x y z"]
        res = []
        cur = ""

        def dfs(i, cur):
            for c in chars[int(digits[i])-2].split():
                if i == len(digits) - 1:
                    res.append(cur + c)
                if i < len(digits) - 1:
                    dfs(i+1, cur + c)
        
        dfs(0, cur)
        return res